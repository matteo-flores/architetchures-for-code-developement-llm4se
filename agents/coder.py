import re
from utils.llm_client import LLMClient

class CoderAgent:

  def __init__(self, llm_client: LLMClient):
    self.llm = llm_client

  def code(self, prompt: str, plan: str, current_code: str, feedback: str) -> str:
    """Generate or fix code based on plan and test feedback."""
    signature = self._extract_signature_from_plan(plan)

    if current_code and feedback:
        full_prompt = self._fix_prompt_template(
            prompt=prompt,
            plan=plan,
            current_code=current_code,
            feedback=feedback,
            signature=signature
        )
    else:
        full_prompt = self._generate_prompt_template(
            prompt=prompt,
            plan=plan,
            signature=signature
        )
    
    response = self.llm.generate_response(full_prompt)
    return self._extract_clean_code(response)

  def _extract_signature_from_plan(self, plan: str) -> str:
    match = re.search(r"SIGNATURE:\s*(def\s+\w+\s*\(.*?\))", plan)
    if match:
        return match.group(1).strip()
    return "def function(...)"



  def _generate_prompt_template(self, *, prompt: str, plan: str, signature: str) -> str:
    return f"""You are an expert Python programmer.

      TASK DESCRIPTION:
      {prompt}
      
      You are given a VERIFIED FUNCTION SIGNATURE and a DETAILED PLAN.
      You MUST follow the plan step by step.
      
      FUNCTION SIGNATURE (use exactly this):
      {signature}
      
      DETAILED PLAN:
      {plan}
      
      Requirements:
      - Write ONLY the function body and signature above
      - Do NOT change the signature
      - Handle all edge cases listed
      - Output ONLY valid Python code
      - Do NOT include explanations, markdown, or extra text
      """


  def _fix_prompt_template(self, *, prompt: str, plan: str, current_code: str, feedback: str, signature: str) -> str:
    return f"""Fix the Python function based on test failures.

      ORIGINAL TASK:
      {prompt}

      FUNCTION SIGNATURE (MUST NOT BE CHANGED):
      {signature}

      DETAILED PLAN (follow exactly):
      {plan}

      PREVIOUS CODE (fix this):
      {current_code}

      TEST FAILURES:
      {feedback}

      Instructions:
      - Rewrite the function using EXACTLY the same signature above
      - Fix only logic or edge cases
      - Do NOT change the function name or parameters
      - Output ONLY valid Python code
      - No explanations or extra text
      """


  def _extract_clean_code(self, response: str) -> str:
    python_block = re.search(
        r"```python\s*(.*?)```",
        response,
        re.DOTALL | re.IGNORECASE
    )
    if python_block:
        return python_block.group(1).strip()
    generic_block = re.search(
        r"```\s*(.*?)```",
        response,
        re.DOTALL
    )
    if generic_block:
        return generic_block.group(1).strip()
    # robust fallback: extract only first function
    lines = response.splitlines()
    code_lines = []
    in_function = False
    for line in lines:
        if line.startswith("def "):
            in_function = True
            code_lines.append(line)
        elif in_function:
            if line.startswith(" ") or line.startswith("\t") or line.strip() == "":
                code_lines.append(line)
            else:
                break
    if code_lines:
        return "\n".join(code_lines).strip()
    raise ValueError("No Python code found in LLM response")


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
    
    if isinstance(response, tuple):
        response = response[0]

            # DEBUG TEMPORANEO
    print("\n===== RAW LLM OUTPUT =====\n")
    print(response)
    print("\n==========================\n")

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
    import re

    # cerca la prima funzione: def <name>(...)
    func_match = re.search(r"(^|\n)(\s*)def\s+\w+\s*\(.*?\)\s*:", response)
    if not func_match:
        # fallback: ritorna tutto se non trova def
        return response.strip()
    
    # estrai tutte le linee a partire dalla def trovata
    start_idx = func_match.start()
    lines = response[start_idx:].splitlines()
    code_lines = []
    indent_level = None

    for line in lines:
        if not code_lines:
            code_lines.append(line)
            # calcola il livello di indent della funzione
            indent_match = re.match(r"(\s*)def\s", line)
            indent_level = len(indent_match.group(1)) if indent_match else 0
        else:
            # accetta linee vuote o linee indentate almeno quanto la funzione
            stripped = line.lstrip()
            curr_indent = len(line) - len(stripped)
            if line.strip() == "" or curr_indent > indent_level:
                code_lines.append(line)
            else:
                break

    return "\n".join(code_lines).rstrip()


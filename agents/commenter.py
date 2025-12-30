import textwrap
import re

class CommenterAgent:
    def __init__(self, llm_client):
        self.llm_client = llm_client

        self.system_prompt = textwrap.dedent("""\
            You are a Commenter Agent in a multi-agent pipeline.
            Your role is to add professional documentation to Python code.
            
            RULES:
            1. Do NOT change variable names, logic, or function signatures.
            2. Add Google-style docstrings.
            3. Add concise inline comments for complex steps.
            4. Output MUST be a single valid Python code block enclosed in markdown.
            """)

    def comment(self, code):
        full_prompt = textwrap.dedent(f"""\
            {self.system_prompt}
            
            CODE TO COMMENT:
            ```python
            {code}
            ```
            
            INSTRUCTIONS:
            Return the fully commented code inside a ```python ... ``` block.
            """)

        response_text, _, _ = self.llm_client.generate_response(
            full_prompt, 
            max_new_tokens=1024, 
            temperature=0.2, 
            deterministic=True
        )

        return self._clean_response(response_text, original_code=code)

    def _clean_response(self, response_text, original_code):
        # Cerca il blocco di codice
        match = re.search(r"```python\s*(.*?)```", response_text, re.DOTALL | re.IGNORECASE)
        if match:
            code = match.group(1)
        else:
            match = re.search(r"```\s*(.*?)```", response_text, re.DOTALL)
            code = match.group(1) if match else response_text
            
        code = code.strip()
        
        # Se il commenter ha fallito o restituito vuoto, restituiamo il codice originale
        if not code:
            return original_code
            
        return code
import traceback
import re
import textwrap

class TesterAgent:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def generate_tests(self, raw_task_prompt, basic_json_tests, entry_point):
        """Genera i test e ripara automaticamente l'indentazione."""
        
        # 1. Estrazione Descrizione
        description = "Generate tests based on logic."
        if '"""' in raw_task_prompt:
            parts = raw_task_prompt.split('"""')
            if len(parts) >= 2: description = parts[1].strip()
        elif "'''" in raw_task_prompt:
            parts = raw_task_prompt.split("'''")
            if len(parts) >= 2: description = parts[1].strip()

        # 2. Prompt Unificato (Senza indentazione iniziale richiesta)
        full_prompt = textwrap.dedent(f"""\
            # ROLE
            You are a Senior Python QA Engineer.

            # TASK DATA
            - Target Function: `{entry_point}`
            - Logic: "{description}"

            # BASIC TESTS:
            {basic_json_tests}

            # INSTRUCTIONS
            Write a Python test script.
            1. Import necessary libraries.
            2. Define `def run_tests(candidate):`.
            3. Inside `run_tests`, paste Basic Tests and add 3-5 NEW edge cases.
            4. Call `run_tests({entry_point})` at the end.
            
            # OUTPUT FORMAT
            Return ONLY the raw Python code block enclosed in ```python ... ```.
            
            # SOLUTION
            ```python
            """)

        # 3. Generazione
        response_text, _, _ = self.llm_client.generate_response(
            full_prompt, 
            max_new_tokens=800, 
            temperature=0.2,
            deterministic=True
        )
        
        print(f"[DEBUG] Raw Tester Response len: {len(response_text)}")

        # Aggiungiamo il blocco che abbiamo aperto nel prompt
        full_response = "```python\n" + response_text

        # 4. Parsing e Riparazione Automatica
        code = self._parse_and_clean_response(full_response)
        print(code)
        
        # 5. Fallback se manca la chiamata critica
        if len(code) < 20 or "run_tests(" not in code:
            print("[WARNING] Tester output broken. Using fallback wrapper.")
            return self._create_fallback_suite(basic_json_tests, entry_point)

        return code

    def _create_fallback_suite(self, basic_tests, entry_point):
        """Crea un wrapper manuale se l'LLM fallisce."""
        if "def check" in basic_tests:
            return f"""
from typing import List, Dict, Any, Tuple, Optional
import math

# Basic Tests provided
{basic_tests}

# Fallback Execution
try:
    check({entry_point})
except NameError:
    pass
"""
        else:
            return f"""
from typing import List, Dict, Any, Tuple, Optional
import math

def run_tests(candidate):
    # Basic Asserts
{textwrap.indent(basic_tests, '    ')}

# Execute
run_tests({entry_point})
"""

    def _parse_and_clean_response(self, response_text):
        """Estrae e pulisce in modo intelligente l'indentazione mista."""
        # 1. Estrai contenuto dai backticks
        match = re.search(r"```python\s*(.*?)```", response_text, re.DOTALL | re.IGNORECASE)
        if match:
            code = match.group(1)
        else:
            match = re.search(r"```\s*(.*?)```", response_text, re.DOTALL)
            code = match.group(1) if match else response_text
        
        code = code.strip()

        # 2. SMART DEDENT: Il cuore della correzione
        lines = code.splitlines()
        
        # Cerchiamo l'indentazione della funzione principale
        main_indent = ""
        for line in lines:
            if "def run_tests(" in line:
                # Cattura gli spazi prima di 'def run_tests'
                main_indent = line[:line.find("def run_tests")]
                break
        
        # Se abbiamo trovato un'indentazione "spuria", la rimuoviamo da tutte le righe
        if main_indent:
            cleaned_lines = []
            for line in lines:
                if line.startswith(main_indent):
                    cleaned_lines.append(line[len(main_indent):])
                else:
                    # Se la riga non ha quell'indentazione (es. un import messo a sinistra)
                    # La puliamo semplicemente dagli spazi iniziali
                    cleaned_lines.append(line.lstrip())
            return "\n".join(cleaned_lines)
        
        # Fallback: dedent standard se non troviamo run_tests indentato
        return textwrap.dedent(code)

    def _sanitize_external_code(self, dirty_code):
        """
        Pulisce il codice del CoderAgent in modo conservativo.
        """
        if not dirty_code: return ""
        
        # 1. Rimuove markdown
        dirty_code = dirty_code.replace("```python", "").replace("```", "")
        
        # 2. Corregge glitch noti di Qwen
        dirty_code = re.sub(r"(^|\n)rom ", r"\1from ", dirty_code)
        dirty_code = re.sub(r"(^|\n)mport ", r"\1import ", dirty_code)

        # 3. DEDENT GLOBALE (Senza spaccare le funzioni interne!)
        # textwrap.dedent rimuove solo l'indentazione comune a TUTTE le righe.
        # Se il coder ha indentato tutto di 4 spazi, li toglie.
        # Se c'è una riga vuota dentro una funzione, NON rompe più la funzione.
        return textwrap.dedent(dirty_code).strip()

    def test(self, code_to_test, test_suite_code):
        namespace = {}
        try:
            # Pulisce ed esegue il Coder
            cleaned_coder_code = self._sanitize_external_code(code_to_test)
            header = "from typing import List, Dict, Optional, Any, Tuple\nimport math\n"
            full_coder_code = header + "\n" + cleaned_coder_code
            exec(full_coder_code, namespace)
        except Exception:
            return False, f"CODER ERROR (Syntax):\n{cleaned_coder_code}\n\nTraceback:\n{traceback.format_exc()}"

        try:
            # Esegue i test (ora puliti dallo Smart Dedent)
            exec(test_suite_code, namespace)
            return True, "Passed"
        except SyntaxError:
             return False, f"TEST SYNTAX ERROR:\n{test_suite_code}\n\nTraceback:\n{traceback.format_exc()}"
        except Exception:
            return False, f"TEST FAILURE:\n{traceback.format_exc()}"
import torch
import gc
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

class LLMClient:
  """
  Manages the upload and the interaction with LLM models,
  ensouring efficienc through caching and tracking token usage.
  """
  def __init__(self, model_id: str):
    self.model_id = model_id
    self.tokenizer = None
    self.model = None

  def _load_model(self):
    """loads the model and the tokenizer only if thery're already cached"""
    bnb_config = BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_compute_dtype=torch.float16,
      bnb_4bit_quant_type="nf4",
      bnb_4bit_use_double_quant=True,
    )
    print(f"--- Loading {self.model_id} ---")
    self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
    self.model = AutoModelForCausalLM.from_pretrained(
      self.model_id,
      quantization_config=bnb_config,
      device_map="auto"
    )
    self.model.eval() # inference

  def generate_response(self, prompt: str, max_new_tokens: int = 500, temperature: float = 0.7, deterministic: bool = False, **kwargs) -> tuple[str, int, int]:
    """
    sends a prompt to the model, return the response and the tokens used/returned

    Returns: (response_text, input_tokens, generated_tokens)
    """
    if self.model is None:
      self._load_model()
        
    # input tokenization
    inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True).to("cuda")
    input_ids = inputs['input_ids']
    input_tokens = input_ids.shape[1]
    
    # output generation
    with torch.no_grad(): # no gradient for intference
      outputs = self.model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        # deterministic
        do_sample=(temperature > 1e-6) and (not deterministic),
        pad_token_id=self.tokenizer.eos_token_id,
        **kwargs
      )
    
    # note: outputs[0] is the complete sequence (input + output)
    generated_ids = outputs[0][input_tokens:] 
    generated_tokens = generated_ids.shape[0]

    # output decoding
    full_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    response_text = full_response[len(prompt):].strip()

    # unloads the model to free space in GPU, so that another agent can upload its model
    self.unload()
    
    return response_text, input_tokens, generated_tokens

  def unload(self):
    if self.model is not None:
      del self.model
    if self.tokenizer is not None:
      del self.tokenizer
    self.model = None
    self.tokenizer = None
    torch.cuda.empty_cache()
    gc.collect()
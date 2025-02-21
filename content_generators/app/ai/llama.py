import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model_id = "meta-llama/Llama-3.2-3B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)

pipe = pipeline(
    "text-generation",
    model=AutoModelForCausalLM.from_pretrained(
        model_id,
        load_in_8bit=True,
        device_map="auto"
    ),
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id
)

def get_response(system_config_mesage, prompt):
  messages = [
    {"role": "system", "content": f"You are ClearNews, a news rewriter and analizer. {system_config_mesage}."},
    {"role": "user", "content": prompt}
  ]

  outputs = pipe(
    messages,
    max_new_tokens=512,
  )

  response = outputs[0]["generated_text"][-1]

  return response
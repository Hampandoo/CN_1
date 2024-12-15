import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-3B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

def get_response(system_config_mesage, prompt):
  messages = [
    {"role": "system", "content": f"You are ClearNews, a news rewriter and analizer. {system_config_mesage}"},
    {"role": "user", "content": prompt}
  ]

  outputs = pipe(
    messages,
    max_new_tokens=256,
  )

  response = outputs[0]["generated_text"][-1]
  print(response)
  return response
from ..ai.llama_3_2_3B import get_response
import os
import json

class LlamaService:
  
  def generate(self, prompt):
    try:
      return get_response(prompt)
    except Exception as e:
      raise e

  def create_system_config_message(self, input_name):
    prompt = self.base_input(input_name)

    return f"{prompt['task']}. {prompt['analysis_requirements']}. Rewrite Requirements: {prompt['rewrite_requirements']}. {prompt['tags']} "
  
  def create_analysis_and_rewrite_prompt(self, input_name, input_text):
    prompt = self.base_input(input_name)
    prompt['input_text'] = input_text

    return f"Text: {prompt['input_text']}"

  def base_input(self, input_name):
    input_path = os.path.join(os.path.dirname(__file__), '../config/inputs.json')
    with open(input_path, 'r') as f:
      input_config = json.load(f)

    return input_config.get(input_name)
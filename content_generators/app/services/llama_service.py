from ..ai.llama import get_response
import os
import json

class LlamaService:
  
  def generate(self, system_config_message, prompt):
    try:
      return get_response(system_config_message, prompt)
    except Exception as e:
      raise e

  def create_system_config_message(self, input_name):
    prompt = self.base_input(input_name)

    schema = f'''
      Please rewrite the news using the following structure and following instructions:\n
      Instruction: \n
      
      {prompt['task']}. {prompt['analysis_requirements']}. {prompt['tags_requirements']}. {prompt['facts_requirements']} 

      Please return the result in the following format:
      ///"contain_data"
        "main_idea": "<Main Idea>",
        "main_facts": [
          "<fact 1>",
          "<fact 2>"
        ],
        "emotional_tone": "<Emotional Tone>",
        "relevant_keywords": [
          "<keyword 1>",
          "<keyword 2>"
        ]
      ///"contain_data"
    '''

    return schema
  
  def create_analysis_and_rewrite_prompt(self, input_name, input_text):
    prompt = self.base_input(input_name)
    prompt['input_text'] = input_text

    return f"Text: {prompt['input_text']}"

  def base_input(self, input_name):
    input_path = os.path.join(os.path.dirname(__file__), '../ai/inputs.json')
    with open(input_path, 'r') as f:
      input_config = json.load(f)

    return input_config.get(input_name)
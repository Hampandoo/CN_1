from .llama_service import LlamaService 

class NewsService:

  def generate_data(self, data):
    llama_service = LlamaService()
    rewrited_data = []
    for item in data:
      full_text = ''
      for text in item["content"]:
        full_text += f"{text} "


      system_config_message = llama_service.create_system_config_message('base_news_prompt')
      prompt = llama_service.create_analysis_and_rewrite_prompt('base_news_prompt', full_text)
      try:
        generated_data = llama_service.generate(system_config_message, f'{prompt} {full_text}')
      except Exception as e:
        raise Exception({ 'error': 'Error generating data', 'details': e })

      rewrited_data.append(
        {
          'content': generated_data,
          'news_id': item['news_id']
        }
      )

    return rewrited_data
from .llama_service import LlamaService 
from app.crud.content import create_content, read_content_paginated
from app.schemas.content import Content as ContentSchema
from app.db.session import SessionLocal
from app.crud.last_date import read_last_date, update_last_date
from app.services.translate_service import TranslateService

from app.utils.helpers import transform_date_to_milliseconds, parse_content
import json

class NewsService:
  def generate_content(self, data):
    llama_service = LlamaService()
    translate_service = TranslateService()
    response = []

    last_date = read_last_date(SessionLocal())
    last_date = transform_date_to_milliseconds(last_date)

    data.news.sort(key=lambda x: transform_date_to_milliseconds(x.date))

    for item in data.news:
      date_to_check = transform_date_to_milliseconds(item.date)

      if last_date >= date_to_check:
        continue

      translated_text = translate_service.transate_text(item.content)

      system_config_message = llama_service.create_system_config_message('base_news_prompt')
      prompt = llama_service.create_analysis_and_rewrite_prompt('base_news_prompt', translated_text)
      try:
        generated_data = llama_service.generate(system_config_message, f'{prompt} {translated_text}')
      except Exception as e:
        print(e)
        raise Exception({ 'error': 'Error generating data', 'details': e })
      
      print('Content generated.')

      try:
        parsed_data = parse_content(generated_data['content'])
        parsed_data["date"] = item.date
      except ValueError as e:
        print(e)
        return str(e)


      resp = create_content(SessionLocal(), parsed_data)

      response.append(resp)

    update_last_date(SessionLocal(), data.news[len(data.news) - 1].date)
    return response
  
  def get_generated_data(self, page, page_size):
    response = read_content_paginated(SessionLocal(), page, page_size)
    return response
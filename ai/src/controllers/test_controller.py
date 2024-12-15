from flask import request, jsonify
from ..service.news_service import NewsService
from ..repositories.news_repository import NewsRepository

class TestController:
  def __init__(self, database):
    self.database = database

  def generate_content(self):
    body = request.get_json()
    if not body:
      return jsonify({'error': f"Validation error", "details": "Request has no data to generate"}), 422
    
    if request.content_type != 'application/json':
      return jsonify({'error': 'Invalid Content-Type header, expected application/json'}), 400

    newsService = NewsService()
    prompt = "Rewrite the main idea and key factors briefly without emotion. At the end, select the following tags or create your own: does not contain useful information, propaganda, paid text, useful information, positive coverage of a person, negative coverage of a person or company. Separately, first write a title that would be suitable for this text"

    #news_repository = NewsRepository(self.database)

    #last_id = news_repository.getHighestId()

    #only_new_data = [d for d in body if int(d['news_id']) > int(last_id)]

    try:
      generated_data = newsService.generate_data(body, prompt)
      print(generated_data)
    except Exception as e:
      return jsonify(e), 500

    try:
      if len(generated_data) > 0:
        #news_repository.saveMany(generated_data)
        print(generated_data)
      return jsonify({'data': generated_data}), 200
    except Exception as e:
      return jsonify({'error': f"Database error", "details": f"Error adding many rows. {str(e)}"}), 500
  

  def get_latest_data(self):
    size = request.args.get('size')
    if type(size) != 'string':
      size = 25
    size = int(size)

    try:
      latest_news = NewsRepository(self.database).get_latest(size)
      news_wo_id = [{ field: value for field, value in news.items() if field != '_id' } for news in latest_news]

      return jsonify({ 'data': news_wo_id }), 200
    except Exception as e:
      return jsonify({'error': f"Database error", "details": f"Error getting latest news. {str(e)}"}), 500
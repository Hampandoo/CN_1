from flask import request, jsonify

from ..utils.helpers import get_site_config 
from ..service.newsService import NewsService
from ..repositories.NewsRepository import NewsRepository

class NewsController:
  def __init__(self, database):
    self.database = database

  def parse(self):
    site_name = request.args.get('site')
    if not site_name:
        return jsonify({'error': 'Site query not provided', 'details': f"Site query is {site_name}"}), 422
  
    try:
      config = get_site_config(site_name)
    except Exception as e:
       return jsonify({'error': 'Site was not found', 'details': str(e)}), 422
    
    try:
      newsService = NewsService(self.database, config)
    except Exception as e:
      return jsonify({'error': f"Error creating parser. {config.get('parserName')}", "details": str(e)}), 500
    
    try:
      links = newsService.get_links()
      parsed_news = newsService.parse_links(links)
    except Exception as e:
      return jsonify({'error': f"Error parsing site. {config.get('parserName')}", "details": str(e)}), 500

    try:
      if len(parsed_news) > 0:
        NewsRepository(self.database).saveMany(parsed_news)

        return jsonify({'data': parsed_news}), 200
      
      return jsonify({ 'data': [], 'message': 'New news not found' }), 200
    except Exception as e:
      return jsonify({'error': f"Database error", "details": f"Could not add many rows to database. {str(e)}"}), 500

  def get_latest_news(self):
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
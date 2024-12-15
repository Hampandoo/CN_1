from ..service.parserService import ParserService
from ..repositories.NewsRepository import NewsRepository

class NewsService:
  def __init__(self, database, config):
    self.database = database
    self.config = config
    self.repository = NewsRepository(database)
    self.parser = ParserService(config).parser

  def get_links(self):
    links = self.parser.get_links()
    only_new_links = []
    highest_saved_id = self.repository.getHighestId()

    for link in links:
      id = self.parser.get_news_id(link)

      if id > int(highest_saved_id):
        only_new_links.append(link)

    return only_new_links
  
  def parse_links(self, links):
    parsed_data = []

    for link in links:
      parsed_content = self.parser.parse_link(link)
      parsed_data.append(parsed_content)

    return parsed_data
    

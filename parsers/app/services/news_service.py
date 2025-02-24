from .parser_service import ParserService
from app.crud.content import create_content
from app.schemas.content import Content as ContentSchema
from ..db.session import SessionLocal
from ..crud.content import create_content, read_content_paginated
from ..crud.last_date import update_last_date

from ..utils.helpers import get_site_config, transform_date_to_milliseconds

class NewsService:
  def __init__(self):
    self.config = get_site_config("interfax")
    self.parserService = ParserService(self.config)
    self.parser = self.parserService.parser

  def get_links(self):
    links = self.parser.get_links(self.parserService.get_last_date())

    return links
  
  def parse_links(self, links):
    parsed_data = []

    for link in links:
      parsed_content = self.parser.parse_link(link)
      parsed_data.append(parsed_content)

    saved_data = []

    # parsed_data.sort(key=lambda x: transform_date_to_milliseconds(x["date"]))
    parsed_data.sort(key=lambda x: x["date"])

    for data in parsed_data:
      resp = create_content(SessionLocal(), data)
      saved_data.append(resp)
    if len(parsed_data) > 0:
      update_last_date(SessionLocal(), self.parserService.config["parserName"], parsed_data[len(parsed_data) - 1]["date"])
    return saved_data
  
  def get_parsed_data(self, page, page_size):
    response = read_content_paginated(SessionLocal(), page, page_size)
    return response
from ..parsers.interfax_parser import InterfaxParser
from ..parsers.ap_parser import APParser
from ..crud.last_date import read_last_date
from ..db.session import SessionLocal

parsers = {
    "interfax": InterfaxParser,
    "ap": APParser
}

class ParserService:
  def __init__(self, config):
     self.config = config
     self.parser = self.create_parser()

  def create_parser(self):
    parser_class_name = self.config.get("parserName")
    parser_class = parsers.get(parser_class_name)

    if not parser_class:
        raise Exception(f"Parser '{parser_class_name}' not found")
    
    parser = parser_class(self.config["url"], self.config["parseUrl"])
    return parser
  def get_last_date(self):
    site_name = self.config["parserName"]
    last_date = read_last_date(SessionLocal(), site_name)
    return last_date
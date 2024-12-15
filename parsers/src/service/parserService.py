from ..parsers.interfax_parser import InterfaxParser

parsers = {
    "interfax": InterfaxParser
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
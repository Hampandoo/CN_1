import json
import os
from datetime import datetime

def get_site_config(site_name: str):
    config_path = os.path.join(os.path.dirname(__file__), '../core/sites_config.json')
    with open(config_path, 'r') as f:
      config = json.load(f)
    site_config = config.get(site_name)
    if site_config == None:
      raise Exception('Config was not found')
    return site_config

def transform_date_to_milliseconds(date_string: str):
   date_object = datetime.strptime(date_string.strip(), "%H:%M %d.%m.%Y")
   milliseconds = int(date_object.timestamp() * 1000)

   return milliseconds
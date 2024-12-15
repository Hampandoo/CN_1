import json
import os

def get_site_config(site_name):
    config_path = os.path.join(os.path.dirname(__file__), '../config/sites.json')
    with open(config_path, 'r') as f:
      config = json.load(f)
    site_config = config.get(site_name)
    if site_config == None:
      raise Exception('Config was not found')
    return site_config
from datetime import datetime
import re
import json

def transform_date_to_milliseconds(date_string: str):
   date_object = datetime.strptime(date_string.strip(), "%H:%M %d.%m.%Y")
   milliseconds = int(date_object.timestamp() * 1000)

   return milliseconds

def parse_content(text: str):
   start_index = text.find('///"contain_data"') + len('///"contain_data"')
   end_index = text.find('///"contain_data"', start_index)
   json_text = text[start_index:end_index].replace("\n", "").strip()
   json_text = '{' + json_text + '}'

   data = json.loads(json_text)
   return data

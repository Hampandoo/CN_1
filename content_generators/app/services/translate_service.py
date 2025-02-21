from langdetect import detect
from app.ai.helsinki_uk_to_en import translate as translate_uk_to_en
import re

class TranslateService:
  def transate_text(self, text: str) -> str:
    lang = detect(text)
    if lang == "uk":
      text = self.clean_text(text)
      translated_text = translate_uk_to_en(text)
      return translated_text
    
    return text
  
  def clean_text(self, text: str) -> str:
    t = re.sub(r"[^\w\s.,!?\"'`-]", " ", text)
    t = re.sub(r"\s+", " ", t)
    return t.strip()
import cloudscraper
from bs4 import BeautifulSoup

HEADERS = {
    'browser': 'chrome',
    'platform': 'windows',
    'desktop': True,
    'mobile': False,
}

class BaseParser:
  def __init__(self, url, url_path):
      self.url = url
      self.url_path = url_path
      self.scraper = cloudscraper.create_scraper(browser=HEADERS)

  def fetch_html(self, url_path=None):
    if url_path == None:
      url_path = self.url_path
    print(self.url + url_path)
    try:
      response = self.scraper.get(self.url + url_path)
      response.raise_for_status()
      return response.text
    except Exception as e:
      raise Exception(f"Error fetching URL {self.url + url_path}: {str(e)}")
      
  def parse_html(self, html):
      soup = BeautifulSoup(html, 'html.parser')
      body_tag = soup.find('body')
      return body_tag
  
  def get_news_id():
     raise Exception("Not Implemented")
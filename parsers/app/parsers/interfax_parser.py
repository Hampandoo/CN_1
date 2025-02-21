from .base_parser import BaseParser
from ..utils.helpers import transform_date_to_milliseconds
from datetime import datetime

class InterfaxParser(BaseParser):
  def __init__(self, url, url_path):
    super().__init__(url, url_path)
    self.schema = {
      'container': 'articles-section-view',
      'link': 'article-link',
      'title': 'article-content-title',
      'content': ['article-content', 'p'],
      'date': ['article-time', 'span']
    }
  
  def get_links(self, parserService):
    html = self.fetch_html()
    soup = self.parse_html(html)

    articles = soup.find('div', class_='articles-section-view')
    new_articles = []

    last_date = parserService.get_last_date()
    last_date = transform_date_to_milliseconds(last_date)

    for article in articles.find_all('div', class_='grid article'):
      time_block = article.find('div', class_='article-time')
      time_block = time_block.find_all('span')

      date = time_block[0].text.strip() + " " + time_block[1].text.strip()
      date = transform_date_to_milliseconds(date)

      if (last_date >= date):
        break
      new_articles.append(article)

    hrefs = []
    for link in new_articles:
      href = link.find(class_ = self.schema['link'])
      hrefs.append(href.get('href'))
    print(hrefs)
    return hrefs

  def parse_link(self, link):
    html = self.fetch_html(link)
    soup = self.parse_html(html)

    title_tag = soup.find(class_ = self.schema['title'])
    title = title_tag.get_text(strip=True) if title_tag else "Title not found"

    content_container = soup.find(class_ = self.schema['content'][0])
    content = ""

    if content_container:
      content_tags = content_container.find_all(self.schema['content'][1])

      for tag in content_tags:
        content += tag.get_text(strip=True)
    else:
      content += "Content not found"

    date_container = soup.find(class_=self.schema["date"][0])
    date = ''
    if date_container:
      date_tags = date_container.find_all(self.schema['date'][1])
      for tag in date_tags:
        date += tag.get_text() + " "

    return {'title': title, 'content': content, 'date': date }
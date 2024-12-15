from .base_parser import BaseParser

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

  def get_news_id(self, link):
    news_link_list = link.split('/')
    news_id = int(news_link_list[-1].split('.html')[0]) 
    return news_id
  
  def get_links(self):
    html = self.fetch_html()
    soup = self.parse_html(html)

    container = soup.find(class_ = self.schema['container'])
    links = container.find_all(class_ = self.schema['link'])

    hrefs = []
    for link in links:
      hrefs.append(link.get('href'))
    return hrefs

  def parse_link(self, link):
    html = self.fetch_html(link)
    soup = self.parse_html(html)

    title_tag = soup.find(class_ = self.schema['title'])
    title = title_tag.get_text(strip=True) if title_tag else "Title not found"

    content_container = soup.find(class_ = self.schema['content'][0])
    content = []

    if content_container:
      content_tags = content_container.find_all(self.schema['content'][1])

      for tag in content_tags:
        content.append(tag.get_text(strip=True))
    else:
      content.append("Content not found")

    date_container = soup.find(class_=self.schema["date"][0])
    date = ''
    if date_container:
      date_tags = date_container.find_all(self.schema['date'][1])
      for tag in date_tags:
        date += tag.get_text() + " "

    # Added news_id
    news_id = self.get_news_id(link)

    return {'title': title, 'content': content, 'date': date, 'news_id': int(news_id)}
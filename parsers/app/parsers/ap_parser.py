from playwright.sync_api import sync_playwright
from .base_parser import BaseParser
from ..utils.helpers import transform_date_to_milliseconds

class APParser(BaseParser):
  def __init__(self, url, url_path):
    super().__init__(url, url_path)
    self.schema = {
      'container': '.PageListStandardD .PageList-items',
      'block': '.PageList-items-item .PagePromo',

      'link': 'article-link',
      'title': 'article-content-title',
      'content': ['article-content', 'p'],
      'date': ['article-time', 'span']
    }


  def get_links(self, last_date):
    def block_resources(route):
      if route.request.resource_type in {"stylesheet", "image", "font"}:
          route.abort()
      else:
          route.continue_()
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1280, "height": 1024},
            java_script_enabled=True,
            ignore_https_errors=True,
            bypass_csp=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        )
        page = context.new_page()

        page.route("**/*", block_resources)

        page.goto(self.url + self.url_path, timeout=60000)
        page.wait_for_selector(self.schema["container"])

        containers = page.query_selector_all(self.schema["container"])
        links = []

        for c in containers:
            blocks = c.query_selector_all(self.schema["block"])

            for b in blocks:
                timestamp = b.get_attribute('data-posted-date-timestamp')

                if last_date >= timestamp:
                    break

                link_element = b.query_selector('.Link')
                if link_element:
                    link = link_element.get_attribute('href')
                    links.append(link)

        browser.close()
        return links
    
  def parse_link(self, link):
    def block_resources(route):
      if route.request.resource_type in {"stylesheet", "image", "font"}:
          route.abort()
      else:
          route.continue_()
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1280, "height": 1024},
            java_script_enabled=True,
            ignore_https_errors=True,
            bypass_csp=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        )
        page = context.new_page()

        try:
            page.route("**/*", block_resources)
            page.goto(link, timeout=60000)

            page.wait_for_selector('.RichTextStoryBody.RichTextBody', timeout=60000)

            date_element = page.query_selector(".Page-dateModified")
            date_element = date_element.query_selector("bsp-timestamp")

            date = date_element.get_attribute("data-timestamp") if date_element else None

            text_blocks = page.query_selector_all("p")
            text = " ".join([t.inner_text() for t in text_blocks]) if text_blocks else ""

            parsed_content = {
                "title": "",
                "content": text,
                "date": date
            }

            return parsed_content

        except Exception as e:
            print(f"Помилка при парсингу {link}: {e}")
            return None

        finally:
            browser.close()
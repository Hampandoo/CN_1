from fastapi import APIRouter, Depends, Query, HTTPException
from app.schemas.content import ContentResponse
from app.services.news_service import NewsService

router = APIRouter()

@router.post("/parse")
def parse():
  newsService = NewsService()

  links = newsService.get_links()
  parsed_news = newsService.parse_links(links)
  return parsed_news

@router.get("/parsed_news")
def get_parsed_news(
  page: int = Query(1, ge=1, description="Page number (starts with 1)"),
  page_size: int = Query(10, ge=1, le=100, description="Count of elements on page"),
):
  newsService = NewsService()
  try:
    response = newsService.get_parsed_data(page, page_size)
  except ValueError as e:
    print(e)
    return HTTPException(status_code=403, detail=str(e))

  if not response.items and page > 1:
    raise HTTPException(status_code=404, detail="Page not found")

  return response
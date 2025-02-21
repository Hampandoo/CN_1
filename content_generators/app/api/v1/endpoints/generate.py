from fastapi import APIRouter, Depends, Query, HTTPException
from app.schemas.content import ContentGenerate, ContentResponse
from app.services.news_service import NewsService

router = APIRouter()

@router.post("/generate")
def generate_content(raw_content: ContentGenerate):
  try:
    content = NewsService().generate_content(raw_content)
    return content
  except ValueError as e:
    print('VALUE ERROR')
    print(e)
    return e

@router.get("/generated_news")
def get_generated_news(
  page: int = Query(1, ge=1, description="Page number (starts with 1)"),
  page_size: int = Query(10, ge=1, le=100, description="Count of elements on page")
):
  newsService = NewsService()
  try:
    response = newsService.get_generated_data(page, page_size)
  except ValueError as e:
    print(e)
    return HTTPException(status_code=403, detail=str(e))

  if not response.items and page > 1:
    raise HTTPException(status_code=404, detail="Page not found")

  return response
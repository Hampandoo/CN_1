from fastapi import APIRouter, Depends, Request, Query
from app.dependencies import get_http_client
from app.config import settings
from httpx import AsyncClient

from app.schema import ContentResponse as ContentResponseSchema

router = APIRouter()

# result for  dependencies=[Depends(verify_user)]
@router.post("/parsers/parse")
async def parsers_parse(
  client: AsyncClient = Depends(get_http_client)
):
  response = await client.post(f"{settings.SERVICE_1_URL}/parsers/parse")
  return response.json()

@router.get("/parsers/parsed_news")
async def parsers_parsed_news(
  page: int = Query(1, ge=1, description="Page number (starts with 1)"),
  page_size: int = Query(10, ge=1, le=100, description="Count of elements on page"),
  client: AsyncClient = Depends(get_http_client)
):
  response = await client.get(f"{settings.SERVICE_1_URL}/parsers/parsed_news?page={page}&page_size={page_size}")
  return response.json()

@router.post("/generators/generate")
async def generators_generate(
  payload: ContentResponseSchema,
  client: AsyncClient = Depends(get_http_client)
):
  response = await client.post(
    f"{settings.SERVICE_2_URL}/generators/generate",
    json=payload.model_dump(),
    timeout=1200.0
  )
  return response.json()

@router.get("/generators/generated_news")
async def parsers_parsed_news(
  page: int = Query(1, ge=1, description="Page number (starts with 1)"),
  page_size: int = Query(10, ge=1, le=100, description="Count of elements on page"),
  client: AsyncClient = Depends(get_http_client)
):
  response = await client.get(f"{settings.SERVICE_2_URL}/generators/generated_news?page={page}&page_size={page_size}")
  return response.json()
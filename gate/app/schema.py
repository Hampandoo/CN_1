from pydantic import BaseModel, Field
from typing import List

class ContentResponseDict(BaseModel):
  title: str
  content: str
  date: str
  id: int

class ContentResponse(BaseModel):
  news: List[ContentResponseDict] = Field(
      ...,
      min_items=0,
      description="List of news items"
    )
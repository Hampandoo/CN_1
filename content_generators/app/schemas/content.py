from pydantic import BaseModel
from typing import List

class Content(BaseModel):
  title: str
  content: str
  date: str
  id: int

  class Config:
    orm_mode = True
    from_attributes=True

class ContentGenerate(BaseModel):
  news: List[Content]
  
class ContentResponseDict(BaseModel):
  date: str
  emotional_tone: str
  main_facts: List[str]
  main_idea: str
  relevant_keywords: List[str]
  id: int

  class Config:
    orm_mode = True
    from_attributes=True

class ContentResponse(BaseModel):
  data: List[ContentResponseDict]

class ContentPaginated(BaseModel):
  items: List[ContentResponseDict]
  total: int
  page: int
  page_size: int

  class Config:
    orm_mode = True
    from_attributes=True
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
  
class ContentResponse(BaseModel):
  data: List[Content]

class ContentPaginated(BaseModel):
  items: List[Content]
  total: int
  page: int
  page_size: int

  class Config:
    orm_mode = True
    from_attributes=True

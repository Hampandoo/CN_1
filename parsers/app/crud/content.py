from sqlalchemy.orm import Session
from app.models.content import Content as ContentModel
from app.schemas.content import Content as ContentShema, ContentResponse as ContentResponseSchema, ContentPaginated as ContentPaginatedSchema

def create_content(db: Session, content: dict) -> ContentModel:
  existing_content = db.query(ContentModel).filter(ContentModel.title == content["title"]).first()
  if existing_content:
    return existing_content

  db_content = ContentModel()
  db_content.title=content["title"]
  db_content.content=content["content"]
  db_content.date=content["date"]

  db.add(db_content)
  db.commit()
  db.refresh(db_content)
  return db_content

def read_content_paginated(db: Session, page: int, page_size: int):
  skip = (page - 1) * page_size
  total = db.query(ContentModel).count()
  items = db.query(ContentModel).offset(skip).limit(page_size).all()

  content_items = [ContentShema.from_orm(item) for item in items]

  return ContentPaginatedSchema(
    items=content_items,
    total=total,
    page=page,
    page_size=page_size
  )
from sqlalchemy.orm import Session
from app.models.content import Content as ContentModel
from app.schemas.content import Content as ContentSchema, ContentResponse as ContentResponseSchema, ContentPaginated as ContentPaginatedSchema, ContentResponseDict as ContentResponseDictSchema

def create_content(db: Session, content: dict) -> ContentModel:
  db_content = ContentModel()
  db_content.emotional_tone=content.get("emotional_tone")
  db_content.main_facts=content.get("main_facts")
  db_content.main_idea=content.get("main_idea")
  db_content.relevant_keywords=content.get("relevant_keywords")
  db_content.date=content.get("date")

  db.add(db_content)
  db.commit()
  db.refresh(db_content)
  return db_content

def read_content_paginated(db: Session, page: int, page_size: int):
  skip = (page - 1) * page_size
  total = db.query(ContentModel).count()
  items = db.query(ContentModel).offset(skip).limit(page_size).all()

  try:
    return ContentPaginatedSchema(
      items=items,
      total=total,
      page=page,
      page_size=page_size
    )
  except Exception as e:
    print(f"Error: {e}")
    return str(e)
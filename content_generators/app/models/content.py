from sqlalchemy import Column, Integer, String, JSON
from app.db.base import Base

class Content(Base):
  __tablename__ = "content"

  id = Column(Integer, primary_key=True, index=True)
  emotional_tone=Column(String, nullable=True)
  main_facts = Column(JSON, nullable=True) 
  main_idea = Column(String, nullable=True)
  relevant_keywords = Column(JSON, nullable=True)
  date = Column(String, index=True, nullable=False)
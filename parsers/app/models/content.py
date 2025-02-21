from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Content(Base):
  __tablename__ = "content"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, unique=False, index=True, nullable=False)
  content = Column(String, index=True, nullable=False)
  date = Column(String, index=True, nullable=False)
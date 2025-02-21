from sqlalchemy import Column, Integer, String
from app.db.base import Base

class LastDate(Base):
  __tablename__ = "lastdate"

  id = Column(Integer, primary_key=True, index=True)
  last_date=Column(String, unique=True, nullable=False)
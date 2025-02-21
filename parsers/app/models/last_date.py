from sqlalchemy import Column, Integer, String
from app.db.base import Base

class LastDate(Base):
  __tablename__ = "lastdate"

  id = Column(Integer, primary_key=True, index=True)
  site_name=Column(String, unique=True, index=True, nullable=False)
  last_date=Column(String, nullable=False)
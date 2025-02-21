from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.base import Base
from ..crud.last_date import initialize_data, delete_all_data

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from app.models.content import Content

Base.metadata.create_all(bind=engine)
# delete_all_data(SessionLocal())
initialize_data(SessionLocal())
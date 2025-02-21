from sqlalchemy.orm import Session
from app.models.last_date import LastDate as LastDateModel

def initialize_data(db: Session):
  try:
    if not db.query(LastDateModel).first():
      initial_data = [
        LastDateModel(site_name="ap", last_date="1738341865000")
      ]
      db.add_all(initial_data)
      db.commit()
      print("Init date added to table")
    else:
      print("Table already has data")
  except Exception as e:
    print(f"Error on initializing data: {e}")
    db.rollback()
  finally:
    db.close()
def delete_all_data(db: Session):
  try:
    db.query(LastDateModel).delete()
    db.commit()
  except Exception as e:
    print(f"Error on deleting all data: {e}")
    db.rollback()

def read_last_date(db:Session, site_name: str):
  record = db.query(LastDateModel).filter(LastDateModel.site_name == site_name).first()
  return record.last_date

def update_last_date(db: Session, site_name: str, date: str):
  last_date_record = db.query(LastDateModel).filter_by(site_name=site_name).first()
  if last_date_record:
    last_date_record.last_date = date
    db.commit()
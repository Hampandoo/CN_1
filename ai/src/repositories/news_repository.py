

class NewsRepository:
  def __init__(self, database):
    self.database = database

  def getHighestId(self):
    if not self.database.db.Rewrited.find_one():
        return 0

    last_news = self.database.db.Rewrited.find().sort('news_id', -1).limit(1)
    last_news = list(last_news)

    last_news_id = last_news[0]['news_id'] if last_news else 0
    return last_news_id

  def saveMany(self, data):
    try:
      result = self.database.db.Rewrited.insert_many(data)
      return result
    except Exception as e:
      raise e
    
  def get_latest(self, size):
    last_records = list(
      self.database.db.Rewrited.find()
      .sort("news_id", -1)
      .limit(size)  
    )

    return last_records
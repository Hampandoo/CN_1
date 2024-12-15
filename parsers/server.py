from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from flask_pymongo import PyMongo
from src.service.parserService import ParserService
from src.controllers.NewsController import NewsController
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/rawNews"
mongo = PyMongo(app)

@app.route('/parse', methods=['GET'])
def parse():
    return NewsController(mongo).parse()

@app.route('/get_latest_news', methods=['GET'])
def get_latest_news():
    return NewsController(mongo).get_latest_news()

def add_test_data():
    if mongo.db.News.count_documents({}) == 0:
        print(mongo.db.News)
        test_data = [
            {"news_id": int("1"), "title": "Test News 1", "content": "This is a test news article."},
        ]
        result = mongo.db.News.insert_many(test_data)
        print(f"Inserted {len(result.inserted_ids)} records")
        print("Test data added.")

add_test_data()

if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 8081))
    app.run(host='0.0.0.0', port=port, debug=True)

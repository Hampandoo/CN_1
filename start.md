cd content_generators
source venv/bin/activate
uvicorn server:app --reload --port 8001

cd parsers
source venv/bin/activate
uvicorn server:app --reload --port 8002

cd gate
source venv/bin/activate
uvicorn server:app --reload

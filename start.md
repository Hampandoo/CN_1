cd content_generators
source generator_venv/bin/activate
uvicorn server:app --reload --port 8001

cd parsers
source parsers_venv/bin/activate
uvicorn server:app --reload --port 8002

cd gate
source gate_venv/bin/activate
uvicorn server:app --reload

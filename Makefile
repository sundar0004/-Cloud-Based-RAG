.PHONY: setup ingest run experiment docker

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

ingest:
	python scripts/ingest.py

run:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

experiment:
	python scripts/run_experiments.py

docker:
	docker compose up --build

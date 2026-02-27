# -Cloud-Based-RAG
Collage project

# MSc Project: Cloud-Based RAG Framework to Reduce LLM Hallucination

This repository contains an end-to-end implementation and documentation package for the MSc final-year project:

**Design and Experimental Evaluation of a Cloud-Based Retrieval-Augmented Generation (RAG) Framework for Reducing Hallucination in Large Language Models**

## 1. Project Objectives
- Build a baseline LLM Q&A system.
- Build a RAG-enhanced Q&A system using local documents.
- Compare baseline vs RAG on factual quality and hallucination behavior.
- Measure retrieval quality, latency, and operational cost signals.
- Package the system for cloud deployment (AWS EC2 / Azure VM) with Docker.

## 2. Tech Stack
- Python 3.10+
- FastAPI
- Sentence Transformers
- FAISS
- Transformers (local HF model) or API model
- Docker / Docker Compose

## 3. Repository Structure
- `src/`: RAG API and modules
- `scripts/`: ingestion and experiment runners
- `experiments/`: sample evaluation dataset
- `docs/`: complete academic document pack
- `data/raw/`: source PDFs/TXT
- `data/processed/`: chunk and index artifacts

## 4. Quick Start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add your documents to `data/raw/`.

Build embeddings + FAISS index:
```bash
PYTHONPATH=. python scripts/ingest.py
```

Run API:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Open Web UI:
`http://127.0.0.1:8000/`

Open Backend API docs:
`http://127.0.0.1:8000/docs`

Try query:
```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query":"What is retrieval-augmented generation?","mode":"rag"}'
```

Run experiments:
```bash
PYTHONPATH=. python scripts/run_experiments.py
```

## Offline Test Mode
If your machine cannot access Hugging Face downloads, use mock mode:
```bash
OFFLINE_MOCK=true PYTHONPATH=. python scripts/ingest.py
OFFLINE_MOCK=true uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## 5. Docker
```bash
docker compose up --build
```

## 6. Academic Pack
Start with:
- `docs/02_proposal.md`
- `docs/03_literature_review.md`
- `docs/05_methodology_and_experiments.md`
- `docs/08_dissertation_template.md`
- `docs/09_viva_prep.md`

## 7. Notes
- This is designed as a strong final-year foundation.
- You should adapt dataset/domain based on your supervisor feedback.
- Keep a weekly log using `docs/10_weekly_progress_template.md`.
- This submission runs on local models; no OpenAI API key is needed.

# Final Submission Document

## Project Title
Design and Experimental Evaluation of a Cloud-Based Retrieval-Augmented Generation (RAG) Framework for Reducing Hallucination in Large Language Models

## Student Details
- Student Name: Sundar A
- College ID: 24207105
- Department: MSc Computer Science
- Institution: Vels University
- Reference Name: Akila
- Email: sunadrsundar0004@gmail.com
- Phone: 7904117804
- GitHub Repository: https://github.com/sundar0004/-Cloud-Based-RAG.git

## Abstract
This project presents a cloud-ready Retrieval-Augmented Generation (RAG) framework designed to reduce hallucination in Large Language Models (LLMs). A baseline generation pipeline and a retrieval-grounded pipeline were developed and compared under a reproducible setup. The system includes document ingestion, chunking, embedding generation, FAISS-based retrieval, context injection, and answer generation. It is exposed through a FastAPI backend with an additional web-based user interface for demonstration. The implementation supports local model execution and an offline mock mode for restricted network environments. The project deliverables include source code, experiment scripts, architecture documentation, viva preparation material, and a complete presentation. The expected outcome is improved factual grounding and reduced hallucination risk compared with baseline generation.

## 1. Introduction
### 1.1 Background
LLMs can generate fluent text but may produce unsupported or fabricated facts (hallucination). This is a major challenge in enterprise and academic applications where factual reliability is required.

### 1.2 Problem Statement
Pure generative responses without evidence retrieval can mislead users. A mechanism is required to ground responses in trusted documents.

### 1.3 Aim
To design and experimentally evaluate a cloud-based RAG framework that improves factual reliability over baseline LLM responses.

### 1.4 Objectives
1. Build baseline LLM question-answering pipeline.
2. Build RAG pipeline with document retrieval.
3. Compare baseline vs RAG using measurable metrics.
4. Deploy as a cloud-ready API and web application.
5. Prepare complete final-year academic artifacts.

## 2. Literature Basis (Concise)
- Transformer foundation: Vaswani et al. (2017).
- Scaled LLM behavior: Brown et al. (2020).
- Retrieval-Augmented Generation: Lewis et al. (2020).
- Dense retrieval methods: Karpukhin et al. (2020).
- Efficient vector search implementation: FAISS.

References list is in `docs/references.md`.

## 3. Proposed System
### 3.1 High-Level Pipeline
User Query -> API Layer -> Retriever -> Top-K Context -> Prompt Construction -> LLM Generation -> Response + Metrics

### 3.2 Workflow
1. Collect source documents (`PDF/TXT/MD`).
2. Extract and normalize text.
3. Chunk documents using fixed window + overlap.
4. Generate embeddings (local sentence-transformer).
5. Store vectors in FAISS index.
6. Retrieve top-k relevant chunks at query time.
7. Inject context into generation prompt.
8. Return answer with latency and retrieved evidence.

### 3.3 Runtime Modes
- Primary mode: local models (no OpenAI key required).
- Offline demo mode: `OFFLINE_MOCK=true`.

## 4. Technology Stack
- Python 3.10+
- FastAPI
- sentence-transformers
- FAISS (faiss-cpu)
- transformers + torch
- Docker / Docker Compose
- Web UI: HTML/CSS/JavaScript

## 5. Implementation Summary
### 5.1 Backend Components
- API entrypoint: `src/main.py`
- Ingestion: `src/ingestion.py`
- Retrieval: `src/retrieval.py`
- Generation: `src/llm.py`
- RAG orchestration: `src/rag_pipeline.py`
- Evaluation helpers: `src/evaluation.py`

### 5.2 Frontend Components
- UI page: `web/index.html`
- Styling: `web/style.css`
- API interaction: `web/app.js`

### 5.3 Experiment Components
- Ingestion runner: `scripts/ingest.py`
- Experiment runner: `scripts/run_experiments.py`
- Dataset: `experiments/questions.json`
- Output: `experiments/results.json`

## 6. API Specification
### 6.1 Health Endpoint
- `GET /health`
- Response: `{"status":"ok"}`

### 6.2 Ask Endpoint
- `POST /ask`
- Body:
```json
{
  "query": "What is retrieval-augmented generation?",
  "mode": "rag",
  "top_k": 4
}
```
- `mode` values: `baseline`, `rag`

### 6.3 Web + Docs
- Frontend: `GET /`
- Swagger: `GET /docs`

## 7. Experimental Plan
### 7.1 Conditions
1. Baseline LLM without retrieval.
2. Basic RAG.
3. Optimized RAG (parameter tuning).

### 7.2 Metrics
- Hallucination proxy score.
- Factual overlap proxy.
- Retrieval precision@k.
- Retrieval recall@k.
- Latency (ms).

### 7.3 Analysis Approach
- Per-question comparison.
- Aggregate averages and variance.
- Error-case analysis for failed retrieval or unsupported claims.

## 8. Cloud Deployment Plan
### 8.1 Dockerized Service
- Build image with `Dockerfile`.
- Start service with `docker-compose.yml`.

### 8.2 VM Deployment
- AWS EC2 or Azure VM.
- Open port 8000 or place reverse proxy.
- Enable TLS for production access.

## 9. Screenshots and Evidence
- Frontend screenshot: `docs/screenshots/frontend_ui.png`
- Backend Swagger screenshot: `docs/screenshots/backend_api_docs.png`
- Presentation file: `docs/MSc_RAG_Project_Vels_University.pptx`

## 10. Results Status
- System structure is complete and runnable.
- Local/offline testing path is available.
- Final dissertation-grade analysis should be completed with domain-specific dataset and recorded results.

## 11. Risks and Limitations
- Metric proxies are approximations of factual truth.
- Domain data quality affects retrieval and answer quality.
- Offline environments can block initial model downloads.

## 12. Ethical Considerations
- Responses must not be treated as guaranteed truth.
- Users should verify critical outputs.
- Sensitive/private data should not be included without authorization.

## 13. Future Scope
- Add citation-focused answer formatting.
- Add reranking for improved retrieval relevance.
- Add human evaluation rubric.
- Optional future extension: OpenAI-based inference integration (not used in current submission).

## 14. Conclusion
This project delivers an end-to-end, cloud-ready RAG framework for hallucination reduction with a working backend, web UI, evaluation pipeline, and complete academic documentation package. It provides a practical foundation for final-year submission and viva demonstration.

## Appendix A: Reproducible Run Commands
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Build index:
```bash
PYTHONPATH=. python scripts/ingest.py
```

Run app:
```bash
PYTHONPATH=. uvicorn src.main:app --host 127.0.0.1 --port 8000
```

Open:
- Frontend: http://127.0.0.1:8000/
- Backend docs: http://127.0.0.1:8000/docs

Offline demo mode:
```bash
OFFLINE_MOCK=true PYTHONPATH=. python scripts/ingest.py
OFFLINE_MOCK=true PYTHONPATH=. uvicorn src.main:app --host 127.0.0.1 --port 8000
```

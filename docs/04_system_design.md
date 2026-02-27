# System Design Document

## 1. Architecture
User -> FastAPI -> Query Router -> Retriever (Embeddings + FAISS) -> Prompt Builder -> LLM -> Response + Metrics

## 2. Components
1. Document Ingestion
- Load PDF/TXT/MD files.
- Normalize and chunk text.
- Build embeddings.
- Persist FAISS index + chunk metadata.

2. Retrieval Module
- Encode user query.
- Similarity search top-k chunks.
- Return chunk text + source path + distance score.

3. Generation Module
- Baseline mode: direct QA prompt.
- RAG mode: context-constrained prompt with retrieved evidence.

4. Evaluation Module
- Factual proxy score.
- Hallucination proxy score.
- Retrieval precision@k and recall@k.
- Latency collection.

5. API Layer
- `/health`
- `/ask` with `baseline` or `rag` mode.

## 3. Deployment
- Dockerized API on VM.
- Volume mapping for data and indexes.
- Optional reverse proxy and TLS in production.

## 4. Non-Functional Requirements
- Reproducibility: deterministic scripts and saved outputs.
- Scalability: index rebuild + containerized deployment.
- Maintainability: modular code and document templates.

import time
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse

from src.rag_pipeline import RAGPipeline
from src.schema import AskRequest, AskResponse, RetrievedChunk

app = FastAPI(title="Cloud RAG Hallucination Reduction API", version="1.0.0")
pipeline = RAGPipeline()
WEB_DIR = Path("web")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home():
    index = WEB_DIR / "index.html"
    if not index.exists():
        return HTMLResponse("<h1>UI not found</h1>", status_code=404)
    return HTMLResponse(index.read_text(encoding="utf-8"))


@app.get("/web/{asset_path:path}")
def web_asset(asset_path: str):
    asset = WEB_DIR / asset_path
    if not asset.exists() or not asset.is_file():
        raise HTTPException(status_code=404, detail="Asset not found")
    return FileResponse(asset)


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest):
    start = time.perf_counter()

    try:
        if payload.mode == "baseline":
            answer, hits = pipeline.answer_baseline(payload.query)
        else:
            answer, hits = pipeline.answer_rag(payload.query, payload.top_k)
    except FileNotFoundError:
        raise HTTPException(
            status_code=400,
            detail="Index not found. Run `python scripts/ingest.py` first.",
        )

    latency_ms = (time.perf_counter() - start) * 1000.0
    retrieved = [RetrievedChunk(**h) for h in hits]

    return AskResponse(
        query=payload.query,
        mode=payload.mode,
        answer=answer,
        latency_ms=latency_ms,
        retrieved=retrieved,
    )

import json
import os
from pathlib import Path
from typing import List, Dict

import faiss
import numpy as np
from PyPDF2 import PdfReader

from src.config import settings
from src.mock_utils import mock_encode, MOCK_DIM


def _read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def load_documents(data_dir: str) -> List[Dict[str, str]]:
    docs = []
    root = Path(data_dir)
    if not root.exists():
        return docs

    for p in root.rglob("*"):
        if not p.is_file():
            continue
        suffix = p.suffix.lower()
        text = ""
        if suffix == ".txt" or suffix == ".md":
            text = _read_text_file(p)
        elif suffix == ".pdf":
            text = _read_pdf(p)

        if text.strip():
            docs.append({"source": str(p), "text": text})
    return docs


def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
    text = " ".join(text.split())
    if not text:
        return []

    chunks = []
    start = 0
    n = len(text)

    while start < n:
        end = min(start + chunk_size, n)
        chunks.append(text[start:end])
        if end >= n:
            break
        start = max(0, end - chunk_overlap)

    return chunks


def build_index() -> Dict[str, int]:
    os.makedirs(settings.processed_dir, exist_ok=True)

    docs = load_documents(settings.data_dir)
    all_chunks = []
    for d in docs:
        chunks = chunk_text(d["text"], settings.chunk_size, settings.chunk_overlap)
        for c in chunks:
            all_chunks.append({"source": d["source"], "text": c})

    if not all_chunks:
        raise ValueError("No documents found. Put .pdf/.txt/.md files in data/raw")

    texts = [c["text"] for c in all_chunks]
    if settings.offline_mock:
        embeddings = mock_encode(texts, dim=MOCK_DIM)
    else:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(settings.embed_model)
        embeddings = model.encode(texts, show_progress_bar=True)
        embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, settings.index_file)
    with open(settings.meta_file, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    return {
        "documents": len(docs),
        "chunks": len(all_chunks),
        "embedding_dim": dim,
    }

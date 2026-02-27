import json
from typing import List, Dict

import faiss
import numpy as np

from src.config import settings
from src.mock_utils import mock_encode, MOCK_DIM


class Retriever:
    def __init__(self):
        self.model = None
        if not settings.offline_mock:
            from sentence_transformers import SentenceTransformer

            self.model = SentenceTransformer(settings.embed_model)
        self.index = faiss.read_index(settings.index_file)
        with open(settings.meta_file, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

    def search(self, query: str, top_k: int | None = None) -> List[Dict]:
        k = top_k or settings.top_k
        if settings.offline_mock:
            q = mock_encode([query], dim=MOCK_DIM)
        else:
            q = self.model.encode([query])
            q = np.array(q).astype("float32")

        distances, indices = self.index.search(q, k)
        results = []
        for score, idx in zip(distances[0], indices[0]):
            if idx < 0 or idx >= len(self.metadata):
                continue
            m = self.metadata[idx]
            results.append(
                {
                    "source": m["source"],
                    "score": float(score),
                    "text": m["text"],
                }
            )
        return results

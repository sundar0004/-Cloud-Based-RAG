import hashlib
from typing import List

import numpy as np


MOCK_DIM = 64


def mock_encode(texts: List[str], dim: int = MOCK_DIM) -> np.ndarray:
    vectors = []
    for text in texts:
        digest = hashlib.sha256(text.encode("utf-8", errors="ignore")).digest()
        raw = (digest * ((dim // len(digest)) + 1))[:dim]
        vec = np.frombuffer(raw, dtype=np.uint8).astype("float32")
        vec = (vec - 127.5) / 127.5
        vectors.append(vec)
    return np.array(vectors, dtype="float32")

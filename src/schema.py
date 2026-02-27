from typing import Literal, List
from pydantic import BaseModel


class AskRequest(BaseModel):
    query: str
    mode: Literal["baseline", "rag"] = "rag"
    top_k: int | None = None


class RetrievedChunk(BaseModel):
    source: str
    score: float
    text: str


class AskResponse(BaseModel):
    query: str
    mode: str
    answer: str
    latency_ms: float
    retrieved: List[RetrievedChunk] = []

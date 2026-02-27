import re
from typing import Dict, List


def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def token_overlap(a: str, b: str) -> float:
    ta = set(normalize(a).split())
    tb = set(normalize(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def factual_proxy(answer: str, ground_truth: str) -> float:
    return token_overlap(answer, ground_truth)


def hallucination_proxy(answer: str, contexts: List[Dict]) -> float:
    if not contexts:
        return 1.0
    joined = " ".join(c["text"] for c in contexts)
    overlap = token_overlap(answer, joined)
    return max(0.0, 1.0 - overlap)


def retrieval_precision_at_k(contexts: List[Dict], relevant_sources: List[str]) -> float:
    if not contexts:
        return 0.0
    hits = sum(1 for c in contexts if c["source"] in set(relevant_sources))
    return hits / len(contexts)


def retrieval_recall_at_k(contexts: List[Dict], relevant_sources: List[str]) -> float:
    if not relevant_sources:
        return 0.0
    unique_retrieved = {c["source"] for c in contexts}
    hits = len(unique_retrieved & set(relevant_sources))
    return hits / len(set(relevant_sources))

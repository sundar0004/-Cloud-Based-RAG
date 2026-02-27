from typing import Tuple, List, Dict

from src.llm import Generator
from src.retrieval import Retriever


class RAGPipeline:
    def __init__(self):
        self.generator = Generator()
        self.retriever = None

    def _get_retriever(self):
        if self.retriever is None:
            self.retriever = Retriever()
        return self.retriever

    @staticmethod
    def _build_baseline_prompt(query: str) -> str:
        return (
            "Answer the question clearly and concisely. "
            "If uncertain, say you are uncertain.\n\n"
            f"Question: {query}\nAnswer:"
        )

    @staticmethod
    def _build_rag_prompt(query: str, contexts: List[Dict]) -> str:
        context_text = "\n\n".join(
            [f"[{i+1}] {c['text']}" for i, c in enumerate(contexts)]
        )
        return (
            "You are a factual assistant. Use only the context below to answer. "
            "If the answer is not in context, say: 'Not found in provided documents.'\n\n"
            f"Context:\n{context_text}\n\n"
            f"Question: {query}\nAnswer:"
        )

    def answer_baseline(self, query: str) -> Tuple[str, List[Dict]]:
        prompt = self._build_baseline_prompt(query)
        return self.generator.generate(prompt), []

    def answer_rag(self, query: str, top_k: int | None = None) -> Tuple[str, List[Dict]]:
        retriever = self._get_retriever()
        hits = retriever.search(query, top_k=top_k)
        prompt = self._build_rag_prompt(query, hits)
        return self.generator.generate(prompt), hits

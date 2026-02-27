import json
import statistics
import time

from src.evaluation import (
    factual_proxy,
    hallucination_proxy,
    retrieval_precision_at_k,
    retrieval_recall_at_k,
)
from src.rag_pipeline import RAGPipeline


def safe_mean(xs):
    return statistics.mean(xs) if xs else 0.0


if __name__ == "__main__":
    with open("experiments/questions.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)

    pipe = RAGPipeline()

    report = {"baseline": [], "rag": []}

    for row in dataset:
        q = row["question"]
        gt = row["ground_truth"]
        relevant_sources = row.get("relevant_sources", [])

        t0 = time.perf_counter()
        b_answer, b_hits = pipe.answer_baseline(q)
        b_latency = (time.perf_counter() - t0) * 1000.0

        report["baseline"].append(
            {
                "id": row["id"],
                "factual": factual_proxy(b_answer, gt),
                "hallucination": hallucination_proxy(b_answer, b_hits),
                "latency_ms": b_latency,
                "precision_at_k": retrieval_precision_at_k(b_hits, relevant_sources),
                "recall_at_k": retrieval_recall_at_k(b_hits, relevant_sources),
                "answer": b_answer,
            }
        )

        try:
            t1 = time.perf_counter()
            r_answer, r_hits = pipe.answer_rag(q)
            r_latency = (time.perf_counter() - t1) * 1000.0

            report["rag"].append(
                {
                    "id": row["id"],
                    "factual": factual_proxy(r_answer, gt),
                    "hallucination": hallucination_proxy(r_answer, r_hits),
                    "latency_ms": r_latency,
                    "precision_at_k": retrieval_precision_at_k(r_hits, relevant_sources),
                    "recall_at_k": retrieval_recall_at_k(r_hits, relevant_sources),
                    "answer": r_answer,
                }
            )
        except FileNotFoundError:
            report["rag"].append(
                {
                    "id": row["id"],
                    "error": "Index not found. Run python scripts/ingest.py first.",
                }
            )

    summary = {}
    for mode in ["baseline", "rag"]:
        rows = [r for r in report[mode] if "error" not in r]
        summary[mode] = {
            "avg_factual": safe_mean([r["factual"] for r in rows]),
            "avg_hallucination": safe_mean([r["hallucination"] for r in rows]),
            "avg_latency_ms": safe_mean([r["latency_ms"] for r in rows]),
            "avg_precision_at_k": safe_mean([r["precision_at_k"] for r in rows]),
            "avg_recall_at_k": safe_mean([r["recall_at_k"] for r in rows]),
        }

    output = {"summary": summary, "details": report}

    with open("experiments/results.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("Experiment complete. Results written to experiments/results.json")
    print(json.dumps(summary, indent=2))

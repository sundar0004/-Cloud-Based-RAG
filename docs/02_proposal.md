# MSc Project Proposal

## 1. Introduction
Generative AI adoption is constrained by unreliable factual behavior in LLM outputs. Retrieval-Augmented Generation (RAG) mitigates this by grounding generation in external evidence. This project proposes a cloud-based RAG framework and a controlled evaluation against non-retrieval baseline generation.

## 2. Research Questions
1. Does RAG reduce hallucination compared with baseline LLM responses?
2. What is the tradeoff between factuality gain and response latency/cost?
3. Which retrieval and context-selection settings produce best performance in this domain?

## 3. Hypotheses
- H1: RAG significantly improves factual accuracy.
- H2: RAG reduces hallucination rate.
- H3: Optimized context selection improves quality with manageable latency overhead.

## 4. Method Summary
- Dataset: curated domain PDFs/TXT + QA set with references.
- Systems: baseline LLM, basic RAG, optimized RAG.
- Metrics: hallucination proxy, factual score, precision@k, recall@k, latency.
- Analysis: per-question results, aggregate mean, significance checks where feasible.

## 5. Tools and Infrastructure
- Python, FastAPI, sentence-transformers, FAISS, transformers.
- Dockerized deployment on AWS EC2 or Azure VM.
- Experiment logging to JSON/CSV.

## 6. Expected Contributions
- A reproducible cloud-ready RAG reference architecture.
- Empirical comparison of hallucination behavior across configurations.
- Practical guidance for enterprise knowledge-grounded assistants.

## 7. Timeline
See `docs/06_execution_timeline.md`.

## 8. Risks
See `docs/07_risk_ethics_budget.md`.

# Methodology and Experiment Plan

## 1. Experimental Conditions
1. Baseline LLM (no retrieval)
2. Basic RAG (default chunking and top-k)
3. Optimized RAG (tuned chunk size, overlap, reranking/context filtering)

## 2. Dataset Strategy
- Domain documents: policy manuals, reports, technical docs.
- QA set: question, gold answer, relevant sources.
- Split: pilot set for tuning, holdout set for final reporting.

## 3. Evaluation Metrics
- Hallucination proxy (lower is better).
- Factual score proxy (higher is better).
- Retrieval precision@k and recall@k.
- Latency in milliseconds.
- Optional human scoring for citation correctness.

## 4. Procedure
1. Ingest corpus and build index.
2. Run baseline responses for all queries.
3. Run basic RAG responses.
4. Run optimized RAG responses.
5. Aggregate metrics and compare deltas.
6. Analyze error cases (missing evidence, irrelevant retrieval, prompt failure).

## 5. Statistical Reporting
- Mean, median, standard deviation.
- Per-question win/loss analysis.
- If sample size allows: paired significance test.

## 6. Threats to Validity
- Proxy metrics may not perfectly capture factual truth.
- Domain dataset quality can bias conclusions.
- Model selection can impact generalizability.

## 7. Reproducibility Checklist
- Fixed dataset version.
- Saved configuration values.
- Stored raw outputs and scripts.
- Version-controlled code and docs.

# Literature Review (Focused)

## 1. Core Background
- Transformer architecture enables modern LLMs (Vaswani et al., 2017).
- GPT-style scaling demonstrated strong zero/few-shot behavior (Brown et al., 2020).
- Hallucination remains a persistent issue in generation tasks.

## 2. Retrieval-Augmented Generation
- RAG combines parametric memory (LM weights) with non-parametric memory (retriever/index) (Lewis et al., 2020).
- Dense passage retrieval supports semantic search at scale (Karpukhin et al., 2020).
- FAISS provides efficient vector similarity indexing for nearest-neighbor retrieval.

## 3. Hallucination and Factuality Evaluation
- Hallucination benchmarks and evaluation methods indicate factuality is multi-dimensional.
- Proxy metrics often combine lexical overlap, entailment, and source attribution checks.
- Human evaluation remains useful for high-stakes claims.

## 4. Gaps Motivating This Project
- Many studies focus on static benchmark datasets rather than cloud-deployed reproducible systems.
- Final-year projects often lack end-to-end engineering + experimental rigor.
- Need for reproducible academic workflow: implementation + comparative evaluation + report artifacts.

## 5. Positioning of This Work
This project contributes a practical, cloud-ready, experimentally evaluated RAG system with an explicit baseline and optimization stages.

## 6. Key References
- Vaswani et al. (2017), *Attention Is All You Need*.
- Brown et al. (2020), *Language Models are Few-Shot Learners*.
- Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Karpukhin et al. (2020), *Dense Passage Retrieval for Open-Domain QA*.
- FAISS documentation and engineering paper.

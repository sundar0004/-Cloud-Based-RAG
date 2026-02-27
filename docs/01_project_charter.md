# Project Charter

## Title
Design and Experimental Evaluation of a Cloud-Based Retrieval-Augmented Generation (RAG) Framework for Reducing Hallucination in Large Language Models

## Problem Statement
Large Language Models (LLMs) can produce fluent but factually incorrect outputs (hallucinations). This limits their adoption in enterprise and decision-support environments.

## Aim
Design, implement, and experimentally evaluate a cloud-deployable RAG framework that improves factual grounding compared with a baseline LLM.

## Objectives
1. Build baseline LLM QA pipeline without retrieval.
2. Build RAG pipeline using FAISS and sentence embeddings.
3. Evaluate factual accuracy, hallucination behavior, retrieval quality, and latency.
4. Deploy containerized service on cloud VM.
5. Produce reproducible academic and technical documentation.

## Scope
- In-scope: single-domain document QA, controlled experiments, API deployment.
- Out-of-scope: large-scale multi-tenant production hardening, human clinical/legal decision automation.

## Deliverables
- Source code + API + Docker setup.
- Experiment dataset and results.
- Dissertation chapters and viva material.
- Risk/ethics and project management artifacts.

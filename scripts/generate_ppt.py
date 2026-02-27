from datetime import date
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt


OUT_FILE = "docs/MSc_RAG_Project_Vels_University.pptx"
STUDENT_NAME = "Sundar A"
COLLEGE_ID = "24207105"
EMAIL = "sunadrsundar0004@gmail.com"
PHONE = "7904117804"
DEPARTMENT = "MSc Computer Science"
REFERENCE_NAME = "Akila"
GITHUB_REPO = "https://github.com/sundar0004/-Cloud-Based-RAG.git"


def add_title_slide(prs, title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle


def add_bullets_slide(prs, title, bullets):
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title
    tf = slide.shapes.placeholders[1].text_frame
    tf.clear()
    for i, b in enumerate(bullets):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = b
        p.level = 0
        p.font.size = Pt(22)


def add_two_column_slide(prs, title, left_title, left_points, right_title, right_points):
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = title

    left_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.6), Inches(6.0), Inches(4.8))
    right_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.6), Inches(6.0), Inches(4.8))

    ltf = left_box.text_frame
    ltf.text = left_title
    ltf.paragraphs[0].font.bold = True
    ltf.paragraphs[0].font.size = Pt(24)
    for pt in left_points:
        p = ltf.add_paragraph()
        p.text = pt
        p.level = 0
        p.font.size = Pt(20)

    rtf = right_box.text_frame
    rtf.text = right_title
    rtf.paragraphs[0].font.bold = True
    rtf.paragraphs[0].font.size = Pt(24)
    for pt in right_points:
        p = rtf.add_paragraph()
        p.text = pt
        p.level = 0
        p.font.size = Pt(20)


def add_image_slide(prs, title, image_path, caption):
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = title
    if Path(image_path).exists():
        slide.shapes.add_picture(image_path, Inches(0.6), Inches(1.3), Inches(12.1), Inches(5.6))
    cap = slide.shapes.add_textbox(Inches(0.6), Inches(7.0), Inches(12.1), Inches(0.5))
    tf = cap.text_frame
    tf.text = caption
    tf.paragraphs[0].font.size = Pt(14)


def build_deck():
    prs = Presentation()

    add_title_slide(
        prs,
        "Design and Experimental Evaluation of a Cloud-Based RAG Framework",
        "Reducing Hallucination in Large Language Models\nMSc Final Year Project | Vels University",
    )

    add_bullets_slide(prs, "Presenter Details", [
        f"Student Name: {STUDENT_NAME}",
        f"College ID: {COLLEGE_ID}",
        f"Department: {DEPARTMENT}",
        "Institution: Vels University",
        f"Reference Name: {REFERENCE_NAME}",
        f"Presentation Date: {date.today().isoformat()}",
    ])

    add_bullets_slide(prs, "Contact and Repository", [
        f"Email: {EMAIL}",
        f"Phone: {PHONE}",
        f"GitHub Repository: {GITHUB_REPO}",
    ])

    add_bullets_slide(prs, "Agenda", [
        "Problem and motivation",
        "Research objectives and questions",
        "System architecture and implementation",
        "Experiments and evaluation metrics",
        "Results, limitations, and future work",
    ])

    add_bullets_slide(prs, "Problem Statement", [
        "LLMs can generate fluent but factually incorrect responses",
        "Hallucination is a major blocker for enterprise adoption",
        "Pure prompt engineering is often insufficient",
        "Need retrieval-grounded generation for reliability",
    ])

    add_bullets_slide(prs, "Project Aim and Objectives", [
        "Design a cloud-based RAG framework",
        "Compare baseline LLM vs RAG-enhanced LLM",
        "Measure factuality, hallucination, retrieval quality, and latency",
        "Deliver a reproducible API + Docker deployment",
    ])

    add_bullets_slide(prs, "Research Questions", [
        "RQ1: Does RAG reduce hallucination vs baseline LLM?",
        "RQ2: What latency tradeoff does retrieval introduce?",
        "RQ3: Which context settings improve answer quality most?",
    ])

    add_bullets_slide(prs, "Literature Foundation", [
        "Transformers: Attention Is All You Need (2017)",
        "LLM scaling: GPT few-shot learning (2020)",
        "RAG for knowledge-intensive tasks (2020)",
        "Dense retrieval and vector search (DPR + FAISS)",
    ])

    add_bullets_slide(prs, "Proposed Workflow", [
        "Document collection (PDF/TXT/MD)",
        "Text extraction and chunking",
        "Embedding generation (Sentence Transformers)",
        "FAISS indexing and top-k retrieval",
        "Context injection and LLM answer generation",
        "Evaluation and comparison",
    ])

    add_bullets_slide(prs, "System Architecture", [
        "User -> FastAPI API Layer",
        "Query Encoder -> FAISS Vector Search",
        "Top-k Context Retrieval",
        "Prompt Builder -> LLM Generator",
        "Evaluation Module -> Response + Metrics",
    ])

    add_two_column_slide(
        prs,
        "Baseline vs RAG",
        "Baseline LLM",
        [
            "Direct question to model",
            "No external evidence grounding",
            "Lower latency",
            "Higher hallucination risk",
        ],
        "RAG LLM",
        [
            "Retrieves relevant evidence",
            "Context-grounded answer generation",
            "Slight latency overhead",
            "Better factual reliability",
        ],
    )

    add_bullets_slide(prs, "Technology Stack", [
        "Python, FastAPI",
        "Sentence Transformers (embeddings)",
        "FAISS (vector database)",
        "Transformers (generator model)",
        "Docker + AWS EC2 / Azure VM",
    ])

    add_bullets_slide(prs, "Experimental Strategy", [
        "Experiment 1: Baseline LLM",
        "Experiment 2: Basic RAG",
        "Experiment 3: Optimized RAG",
        "Compare quality and latency across all setups",
    ])

    add_bullets_slide(prs, "Evaluation Metrics", [
        "Hallucination Rate (proxy)",
        "Factual Accuracy (proxy)",
        "Precision@K and Recall@K (retrieval quality)",
        "Latency (ms) and computational cost",
    ])

    add_bullets_slide(prs, "Implementation Deliverables", [
        "Document ingestion script",
        "FAISS indexing pipeline",
        "API endpoint for baseline and RAG queries",
        "Experiment runner with JSON result output",
        "Dockerized cloud deployment setup",
    ])

    add_image_slide(
        prs,
        "Frontend UI Screenshot",
        "docs/screenshots/frontend_ui.png",
        "Figure: Web UI showing query input, answer output, and retrieved context.",
    )

    add_image_slide(
        prs,
        "Backend API Screenshot",
        "docs/screenshots/backend_api_docs.png",
        "Figure: FastAPI Swagger docs for backend testing and endpoint validation.",
    )

    add_bullets_slide(prs, "Six-Month Timeline", [
        "Month 1: Fundamentals + literature review",
        "Month 2: Ingestion and indexing",
        "Month 3: Baseline + RAG implementation",
        "Month 4: Evaluation module and tuning",
        "Month 5: Cloud deployment and full testing",
        "Month 6: Final experiments + dissertation + viva",
    ])

    add_bullets_slide(prs, "Risks and Mitigation", [
        "Data quality risk -> source validation",
        "Model/runtime limits -> lighter model fallback",
        "Cloud security risk -> least privilege and TLS",
        "Schedule overrun -> weekly milestone tracking",
    ])

    add_bullets_slide(prs, "Expected Outcomes", [
        "Measured reduction in hallucination with RAG",
        "Improved factual grounding and answer trustworthiness",
        "Reproducible academic and technical artifacts",
        "Practical guidance for enterprise AI assistants",
    ])

    add_bullets_slide(prs, "Conclusion", [
        "RAG is a practical method to improve factual reliability",
        "This project combines engineering and experimental rigor",
        "Framework is cloud-ready and reproducible",
        "Future work: reranking, citation verification, human eval",
    ])

    add_bullets_slide(prs, "Thank You", [
        "Questions and Discussion",
        "Supervisor Feedback Welcome",
        "Vels University",
    ])

    prs.save(OUT_FILE)
    print(f"Created: {OUT_FILE}")


if __name__ == "__main__":
    build_deck()

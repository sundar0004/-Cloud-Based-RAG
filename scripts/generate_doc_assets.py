from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


OUT_DIR = Path("docs/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def architecture_diagram(path: Path):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def box(x, y, w, h, label, fc="#e8f1ff"):
        patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                               linewidth=1.5, edgecolor="#2b4c7e", facecolor=fc)
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=10)

    box(0.5, 3.2, 1.8, 1.0, "User / UI")
    box(3.0, 3.2, 2.0, 1.0, "FastAPI\nBackend")
    box(5.7, 3.2, 1.8, 1.0, "Retriever")
    box(8.2, 3.2, 2.0, 1.0, "FAISS\nIndex")
    box(10.9, 3.2, 2.0, 1.0, "Local LLM")

    box(3.0, 1.0, 2.2, 1.0, "Ingestion")
    box(5.9, 1.0, 2.2, 1.0, "Embeddings")
    box(8.8, 1.0, 2.2, 1.0, "Metadata")

    ax.annotate("", xy=(3.0, 3.7), xytext=(2.3, 3.7), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(5.7, 3.7), xytext=(5.0, 3.7), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(8.2, 3.7), xytext=(7.5, 3.7), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(10.9, 3.7), xytext=(10.2, 3.7), arrowprops=dict(arrowstyle="->", lw=1.5))

    ax.annotate("", xy=(8.8, 2.0), xytext=(10.0, 3.2), arrowprops=dict(arrowstyle="->", lw=1.3, linestyle="--"))
    ax.annotate("", xy=(8.2, 3.2), xytext=(7.0, 2.0), arrowprops=dict(arrowstyle="->", lw=1.3, linestyle="--"))

    ax.annotate("", xy=(5.9, 1.5), xytext=(5.2, 1.5), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(8.8, 1.5), xytext=(8.1, 1.5), arrowprops=dict(arrowstyle="->", lw=1.5))

    ax.set_title("Project Architecture Diagram", fontsize=16, weight="bold")
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def metrics_graph(path: Path):
    labels = ["Factual\n(↑)", "Hallucination\n(↓)", "Precision@k\n(↑)", "Recall@k\n(↑)"]
    baseline = [0.46, 0.58, 0.30, 0.34]
    rag = [0.74, 0.29, 0.68, 0.72]

    x = range(len(labels))
    width = 0.36

    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.bar([i - width / 2 for i in x], baseline, width=width, label="Baseline", color="#8ba7c7")
    ax.bar([i + width / 2 for i in x], rag, width=width, label="RAG", color="#1f77b4")

    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Normalized Score")
    ax.set_title("Comparative Performance Overview (Illustrative)")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.3)

    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def main():
    architecture_diagram(OUT_DIR / "architecture_diagram.png")
    metrics_graph(OUT_DIR / "results_graph.png")
    print("Created diagram assets in docs/figures")


if __name__ == "__main__":
    main()

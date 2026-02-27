from src.ingestion import build_index


if __name__ == "__main__":
    stats = build_index()
    print("Index build complete:")
    for k, v in stats.items():
        print(f"- {k}: {v}")

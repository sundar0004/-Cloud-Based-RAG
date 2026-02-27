import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    offline_mock: bool = os.getenv("OFFLINE_MOCK", "false").lower() == "true"
    embed_model: str = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    gen_model: str = os.getenv("GEN_MODEL", "google/flan-t5-base")
    top_k: int = int(os.getenv("TOP_K", "4"))
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "800"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "120"))
    data_dir: str = os.getenv("DATA_DIR", "data/raw")
    processed_dir: str = os.getenv("PROCESSED_DIR", "data/processed")
    index_file: str = os.getenv("INDEX_FILE", "data/processed/faiss.index")
    meta_file: str = os.getenv("META_FILE", "data/processed/chunks.json")


settings = Settings()

from transformers import pipeline

from src.config import settings


class Generator:
    def __init__(self):
        self.pipe = None
        if not settings.offline_mock:
            self.pipe = pipeline(
                "text2text-generation",
                model=settings.gen_model,
                max_new_tokens=256,
            )

    def generate(self, prompt: str) -> str:
        if settings.offline_mock:
            return "Mock response (offline mode): retrieved context used for grounded answering."
        out = self.pipe(prompt)
        return out[0]["generated_text"].strip()

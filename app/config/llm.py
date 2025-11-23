from llama_cpp import Llama
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # this gives /app
MODEL_PATH = BASE_DIR / "llm_models" / "phi3-q4.gguf"

def getllm():
    return Llama(
        model_path=str(MODEL_PATH),
        n_ctx=4096,
        n_threads=8,       # M1/M2/M3 CPU will use 8 cores
        temperature=0.2
    )

llm = getllm()

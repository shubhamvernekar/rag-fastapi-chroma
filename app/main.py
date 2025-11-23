from fastapi import FastAPI
from ingest import ingest_controller
from query import query_controller

app = FastAPI(
    title="Phi-RAG",
    description="Local RAG pipeline using FastAPI + Chroma + GGUF LLM",
    version="1.0.0",
)

app.include_router(ingest_controller.ingestRoute)
app.include_router(query_controller.queryRoute)

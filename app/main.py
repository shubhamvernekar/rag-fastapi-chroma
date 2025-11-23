from query import query_controller
from fastapi import FastAPI
from dotenv import load_dotenv
from ingest import ingest_controller

load_dotenv()
app = FastAPI()

app.include_router(ingest_controller.ingestRoute)
app.include_router(query_controller.queryRoute)

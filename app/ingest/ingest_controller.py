from ingest.ingest_service import ingestFile
from fastapi import UploadFile, File, HTTPException, APIRouter

ingestRoute = APIRouter(prefix="/ingest")

@ingestRoute.post("/")
async def ingest(file: UploadFile = File(...)):
    try:
        print("Ingesting file name: ", file.filename, " size:", file.size / (1024 * 1024), " mb")
        count = await ingestFile(file)
        print(f"Saved doc chunks = {count}")
        return {"message": "File ingested successfully"}
    except Exception as e:
        print(f"Error: ", str(e))
        raise HTTPException(status_code=500, detail=str(e))

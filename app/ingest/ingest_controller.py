from ingest.ingest_service import ingestFile
from fastapi import UploadFile, File, HTTPException, APIRouter

ingestRoute = APIRouter(prefix="/ingest")

@ingestRoute.post("/")
async def ingest(file: UploadFile = File(...)):
    try:
        file_size_mb = file.size / (1024 * 1024)
        print(f"Ingesting: {file.filename} ({file_size_mb:.2f} MB)")

        count = await ingestFile(file)
        print(f"Saved doc chunks = {count}")

        return {"message": f"File ingested successfully ({count} chunks)"}
    except Exception as e:
        print(f"Error ingesting file: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

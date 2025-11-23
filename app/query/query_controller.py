from query.query_model import QueryRequest
from rag.rag_service import generateAnswer, retriveContext
from fastapi import APIRouter, HTTPException

queryRoute = APIRouter(prefix="/query")

@queryRoute.get("/")
async def query(body: QueryRequest):
    try:
        q = body.question

        docs = retriveContext(q)
        if not docs:
            return {"answer": "No relevant information found in documents"}
        
        response = await generateAnswer(q, docs)
        return {"answer": response}
    except Exception as e:
        print(f"Error: ", str(e))
        raise HTTPException(status_code=500, detail=str(e))

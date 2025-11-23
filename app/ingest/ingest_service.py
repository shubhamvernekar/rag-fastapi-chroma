from rag.splitter import splitDocuments
from rag.vector_store import storeDocuments
from fastapi import UploadFile
from rag.loader import loadDocument


async def ingestFile(file: UploadFile):
    docs = await loadDocument(file)

    if not docs:
        raise ValueError("No text extracted from document")

    chunks = splitDocuments(docs)
    
    if not chunks:
        raise ValueError("Failed to split document into chunks")

    count = storeDocuments(chunks)
    return count

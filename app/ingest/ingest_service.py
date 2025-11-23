

from rag.splitter import splitDocuments
from rag.vector_store import storeDocuments
from fastapi import UploadFile
from rag.loader import loadDocument


async def ingestFile(file: UploadFile):
    docs = await loadDocument(file)
    chunks = splitDocuments(docs)
    count = storeDocuments(chunks)
    return count

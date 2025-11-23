import os
from plistlib import InvalidFileException
from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader, TextLoader

async def loadDocument(file: UploadFile):
    ext = file.filename.split('.')[-1].lower()
    temp_path = f"/tmp/{file.filename}"

    with open(temp_path, "wb") as f:
        f.write(await file.read())

    if ext == "pdf":
        loader = PyPDFLoader(temp_path)
    elif ext == "txt":
        loader = TextLoader(temp_path)
    else:
        raise InvalidFileException(f"Unsupported file type: {ext}")

    docs = loader.load()
    os.remove(temp_path)

    return docs

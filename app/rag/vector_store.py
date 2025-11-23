from .embedding import getEmbeddingModel
from langchain_chroma import Chroma

PERSIST_DIR = "vector_dir"

def storeDocuments(docs):
    embeddings = getEmbeddingModel()
    db = Chroma(
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR
    )
    db.add_documents(docs)
    return len(docs)

def getVectorStore():
    embeddings = getEmbeddingModel()
    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )

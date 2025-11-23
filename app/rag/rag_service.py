

from pydoc import doc
from config.llm import llm
from .vector_store import getVectorStore

def retriveContext(query: str, k: int = 4):
    db = getVectorStore();
    docs = db.similarity_search(query, k=k)
    return docs

async def generateAnswer(query: str, context_docs):
    context_text = "\n\n".join([d.page_content for d in context_docs])
    prompt = f"""
    You are an assistant that answers strictly using the provided internal company documents

    ### CONTEXT:
    {context_text}

    ###QUESTION:
    {query}

    ###RULES
    - If context contains answer - answer precisely.
    - If answer not found -> say "I counldn't found answer in company documents"

    Final answer:
    """
    response = llm(
        prompt,
        max_tokens=300,
        stop=["</s>"]
    )
    print("Response ", response)
    return response["choices"][0]["text"]
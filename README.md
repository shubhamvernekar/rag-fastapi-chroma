Phi-RAG – Simple Local RAG Service

A lightweight Retrieval-Augmented Generation (RAG) system using:
  - FastAPI
  - ChromaDB
  - LangChain
  - Local GGUF LLM (Phi-3 / any GGUF model)
Runs fully offline and is easy to set up.

📁 Project Structure
```
app/
├── main.py
├── llm_models/          ← put your .gguf model here
├── vector_dir/          ← chroma DB gets stored here
├── ingest/
├── query/
└── rag/
```

📦 Install Requirements
Create virtual environment (optional):
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

🤖 Add Your Model
Download a GGUF model (example: phi3-q4.gguf)
Place it inside:
```
app/llm_models/
```

Full path should look like:
```
app/llm_models/phi3-q4.gguf
```

▶️ Run the Server
From the project root:
```
uvicorn app.main:app --reload
```

API Docs:
```
http://localhost:8000/docs
```

📥 Ingest a Document
Use the /ingest API:
```
POST /ingest
```
Upload file as form-data:
```
file = your_document.pdf
```
The embeddings are stored locally in:
```
app/vector_dir/
```

🔍 Query
Ask a question:
```
GET /query/
```
Body:
```
{
  "question": "What does the NDA say about confidentiality?"
}
```

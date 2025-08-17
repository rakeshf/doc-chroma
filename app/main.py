# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chromadb.config import Settings
from chromadb import PersistentClient

app = FastAPI(title="ChromaDB Support Bot")

# Initialize ChromaDB client (PersistentClient stores data on disk)
client = PersistentClient(path="./chroma_db")

# Ensure the collection exists
collection_name = "support_docs"
if collection_name not in [c.name for c in client.list_collections()]:
    client.create_collection(name=collection_name)
collection = client.get_collection(collection_name)

# Pydantic models for request bodies
class AddDocumentRequest(BaseModel):
    id: str
    text: str
    metadata: dict = {}

class QueryRequest(BaseModel):
    text: str
    n_results: int = 5
    where: dict = {}

# Endpoint: List all collections
@app.get("/collections")
def list_collections():
    return {"collections": [{"name": c.name} for c in client.list_collections()]}

# Endpoint: Add a document
@app.post("/add")
def add_document(req: AddDocumentRequest):
    try:
        collection.add(
            ids=[req.id],
            documents=[req.text],
            metadatas=[req.metadata]
        )
        return {"message": f"Document '{req.id}' added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Query documents
@app.post("/query")
def query_documents(req: QueryRequest):
    try:
        result = collection.query(
            query_texts=[req.text],
            n_results=req.n_results,
            where=req.where if req.where else None
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

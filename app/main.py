import chromadb

# Connect to ChromaDB server
client = chromadb.HttpClient(host="chromadb", port=8000)

print("✅ Connected to ChromaDB")

# Create or get collection
collection = client.get_or_create_collection("support_docs")

# Add some docs
collection.add(
    documents=["How to reset password?", "Steps to configure API key"],
    metadatas=[{"source": "faq"}, {"source": "docs"}],
    ids=["q1", "q2"]
)

# Query
results = collection.query(query_texts=["reset API key"], n_results=2)
print("🔎 Results:", results)

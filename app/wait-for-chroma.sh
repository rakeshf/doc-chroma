#!/bin/sh
echo "⏳ Waiting for ChromaDB..."
until curl -s http://chromadb:8000/ > /dev/null; do
  echo "ChromaDB not ready yet..."
  sleep 2
done
echo "✅ ChromaDB ready!"
exec uvicorn main:app --host 0.0.0.0 --port 9000

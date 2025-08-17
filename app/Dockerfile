# app/Dockerfile
FROM python:3.11-slim

# Install curl for wait-for script
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x /app/wait-for-chroma.sh

# Run FastAPI app on port 9000
CMD ["./wait-for-chroma.sh", "chromadb:8000", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]

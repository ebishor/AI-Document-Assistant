# AI-Document-Assistant
Tech Stack
Frontend: React
Backend: FastAPI or Spring Boot
LLM: Llama 3.1 / GPT-4o
Embeddings: BGE or text-embedding-3-large
Vector DB: PostgreSQL + pgvector / ChromaDB
Queue: RabbitMQ
Docker
Kubernetes
Prometheus + Grafana

ARCHITECTURE: 
                      React Frontend
                           │
                           │
                     FastAPI Gateway
                           │
        ┌──────────────────┼─────────────────┐
        │                  │                 │
        │                  │                 │
 Document Service     Chat Service     Authentication
        │                  │
        │                  │
Embedding Service     LLM Service
        │
        │
 Vector Database (pgvector)

        │
 PostgreSQL

        │
 RabbitMQ Worker

        │
 File Processing


 Folder Structure:

 AI-Document-Assistant/

│

├── frontend/

├── api-gateway/

├── chat-service/

├── embedding-service/

├── document-service/

├── auth-service/

├── worker/

├── postgres/

├── docker/

├── kubernetes/

├── monitoring/

├── docs/

├── tests/

└── README.md

Pre Requisites:
Please install and verify the following:

✅ Python 3.11
✅ VS Code + Python, Docker, Kubernetes, YAML extensions
✅ Git
✅ Docker Desktop (verify docker run hello-world)
✅ Enable WSL 2 if you're on Windows (Docker Desktop performs best with it)
✅ Node.js LTS
✅ PostgreSQL 15 or 16
✅ Postman
✅ Ollama (optional but recommended)
# 🧠 GENAI-PROJECT — Generative AI Knowledge Base Chatbot

## 📘 Overview
The **GenAI Project** is a Flask-based Generative AI system designed to:
- Ingest and extract knowledge from **PDF files**
- Store embeddings in a **PostgreSQL database** using vector similarity
- Answer user queries via **semantic search and large language models (LLMs)**
- Provide REST APIs for interaction and integration

This setup supports a **Knowledge Base creation workflow** and **LLM-powered question answering**.

---

## 🏗️ Project Structure
```
GenAI_PJ/
│
├── docker-compose.yml              # Docker setup (Flask API + PostgreSQL + pgvector)
│
├── api/
│   ├── main.py                     # Flask API entry point
│   ├── aiservice.py                # Handles LLM and intent classification
│   ├── contants.py                 # System prompt and configuration constants
│   ├── utils.py                    # JSON and data extraction helpers
│   │
│   ├── kb_service/                 # Knowledge Base Service Layer
│   │   ├── DBService.py            # PostgreSQL database connection manager
│   │   ├── Embedding.py            # Embedding generation and database insertion
│   │   ├── pdf_extraction.py       # Extracts text content from PDFs
│   │   ├── similarity_search.py    # Vector-based similarity search in the DB
│   │   ├── Requirement.txt         # Dependencies for the KB service
│   │   ├── assets/                 # Sample extracted text data
│   │   └── __init__.py
│   │
│   └── kb_info/                    # Uploaded knowledge base text data
│       ├── <UUID>_share price.pdf.txt
│       ├── <UUID>_Data Science.pdf.txt
│
└── .env                            # Environment variables (API keys, DB creds)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL with pgvector extension
- Google Generative AI SDK (`google-genai`)

---

### 2️⃣ Environment Variables (`.env`)
```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=genai_db
GOOGLE_API_KEY=your_google_api_key
EMBEDDING_MODEL=models/embedding-001
GENAI_MODEL=gemini-1.5-flash
```

---

### 3️⃣ Install Dependencies
```bash
cd api/kb_service
pip install -r Requirement.txt
```

---

### 4️⃣ Run with Docker
```bash
docker-compose up --build
```

---

## 🚀 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/upload` | POST | Uploads a PDF and extracts its text |
| `/create_kb` | POST | Generates embeddings and stores them in DB |
| `/ask` | POST | Sends a query, performs similarity search, and returns LLM-generated answer |

Example:
```bash
POST /ask
{
  "question": "What is the CGPA of Sermaraj?",
  "session_id": "123"
}
```

---

## 🧩 Core Components
- **`aiservice.py`** — LLM calls for embeddings & intent classification
- **`Embedding.py`** — Generates embeddings and stores them
- **`pdf_extraction.py`** — Extracts text from PDFs
- **`similarity_search.py`** — Semantic search using vector embeddings
- **`main.py`** — Flask routes & orchestration

---

## 🧠 Knowledge Flow
```
PDF → Extract Text → Create Embeddings → Store in DB → User Query → Similarity Search → LLM Answer
```

---

## 🧰 Tech Stack
| Category | Tool |
|-----------|------|
| Framework | Flask |
| Database | PostgreSQL + pgvector |
| LLM API | Google Generative AI |
| Containerization | Docker |
| Language | Python 3.10+ |

---

## 👨‍💻 Notes
- Run locally with `flask run` inside `api/`
- Update `.env` for local/cloud DB
- Clear `embeddings_store` to reset KB

---

## 📄 License
MIT License

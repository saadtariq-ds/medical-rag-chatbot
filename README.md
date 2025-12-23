# 🏥 Medical RAG Chatbot

Medical RAG Chatbot is a **Retrieval-Augmented Generation (RAG)** application that answers medical questions using trusted knowledge extracted from PDF documents (e.g., guidelines, manuals, clinical notes). It combines **Groq LLM**, **Hugging Face embeddings**, **FAISS vector search**, and **LangChain** to provide grounded answers with relevant context.

The app provides a Flask backend API, a lightweight HTML/CSS frontend, containerization with Docker, vulnerability scanning using Trivy, and CI/CD automation via Jenkins for AWS deployment.

---

## ✨ Features

- 📄 Ingest medical PDFs using PyPDF
- 🔍 Semantic retrieval using Hugging Face embeddings + FAISS
- 🤖 Context-grounded answers using Groq LLM
- 🔗 LangChain orchestration for RAG pipeline (retrieval + generation)
- 🌐 Flask API for chat + ingestion endpoints
- 🎨 Simple HTML/CSS web UI
- 🐳 Dockerized application for consistent deployment
- 🔐 Security scanning using Aqua Trivy (Docker image vulnerabilities)
- 🔁 Jenkins CI/CD pipeline for automated build, scan, and deploy
- ☁️ AWS deployment-ready workflow

---

## 🧠 How It Works (RAG Flow)

1. PDFs are loaded and text is extracted using **PyPDF**
2. Text is chunked and embedded using **Hugging Face embeddings**
3. Embeddings are indexed in **FAISS**
4. User query is embedded and matched against FAISS for top relevant chunks
5. Retrieved context is passed to the **Groq LLM** via **LangChain**
6. Chatbot returns an answer grounded in retrieved evidence

---

## 🧱 Tech Stack

| Category | Tools |
|---------|------|
| LLMs | Groq |
| Embeddings | Hugging Face |
| RAG Framework | LangChain |
| Vector Store | FAISS (local) |
| PDF Processing | PyPDF |
| Backend | Flask |
| Frontend | HTML / CSS |
| Containerization | Docker |
| Security Scanning | Aqua Trivy |
| CI/CD | Jenkins |
| Cloud | AWS |
| SCM | GitHub |

---

# ⚙️ Setup & Run Locally
## 1️⃣ Clone
```bash
git clone https://github.com/your-username/medical-rag-chatbot.git
cd medical-rag-chatbot
```

## 2️⃣ Create virtual environment (recommended)
```bash
python -m venv ven
source venv/bin/activate   # Windows: venv\Scripts\activate
```

## 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

## 4️⃣ Run Flask backend
```bash
python src/api.py
```
Open the UI:
- Serve frontend/index.html (or integrate via Flask templates)
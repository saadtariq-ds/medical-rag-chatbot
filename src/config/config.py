""" Configuration settings for the application. """

import os
from dotenv import load_dotenv
load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.1-8b-instant"

DB_FAISS_PATH: str = "vector_store/db_faiss"
DATA_PATH: str = "data/"

CHUNK_SIZE: int = 500
CHUNK_OVERLAP: int = 50
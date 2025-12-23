""" Vector store component for the medical RAG chatbot. """

import os
from langchain_community.vectorstores import FAISS
from src.components.embeddings import get_embeddings
from src.common.custom_exception import CustomException
from src.common.logger import get_logger
from src.config.config import DB_FAISS_PATH

logger = get_logger(__name__)


def load_vector_store():
    try:
        logger.info("Loading vector store from FAISS database...")
        embeddings = get_embeddings()

        if not os.path.exists(DB_FAISS_PATH):
            logger.error(f"FAISS database path does not exist: {DB_FAISS_PATH}")
            raise CustomException(f"FAISS database path does not exist: {DB_FAISS_PATH}")
        
        vector_store = FAISS.load_local(
            folder_path=DB_FAISS_PATH, 
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )
        logger.info("Vector store loaded successfully.")
        return vector_store

    except Exception as e:
        logger.error(f"Error loading vector store: {e}")
        raise CustomException(f"Error loading vector store: {e}")
    

def create_vector_store(documents):
    try:
        if not documents:
            logger.error("No documents provided to create the vector store.")
            raise CustomException("No documents provided to create the vector store.")
        
        logger.info("Creating vector store...")
        embeddings = get_embeddings()
        vector_store = FAISS.from_documents(documents, embeddings)
        vector_store.save_local(folder_path=DB_FAISS_PATH)
        logger.info("Vector store created and saved successfully.")
        return vector_store

    except Exception as e:
        logger.error(f"Error creating vector store: {e}")
        raise CustomException(f"Error creating vector store: {e}")
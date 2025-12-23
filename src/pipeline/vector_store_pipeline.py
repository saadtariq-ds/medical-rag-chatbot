""" Vector store pipeline for the medical RAG chatbot. """

from src.components.data_loader import load_pdf_files, split_documents
from src.components.vector_store import create_vector_store
from src.common.logger import get_logger
from src.common.custom_exception import CustomException
from src.config.config import DB_FAISS_PATH

logger = get_logger(__name__)


def setup_vector_store_pipeline():
    try:
        logger.info("Starting vector store setup pipeline...")

        # Load PDF files
        documents = load_pdf_files()

        # Split documents into chunks
        text_chunks = split_documents(documents=documents)

        # Create vector store from document chunks
        vector_store = create_vector_store(documents=text_chunks)

        logger.info("Vector store setup pipeline completed successfully.")
        return vector_store

    except Exception as e:
        logger.error(f"Unexpected error in vector store pipeline: {e}")
        raise CustomException(f"Unexpected error in vector store pipeline: {e}")
    
if __name__ == "__main__":
    setup_vector_store_pipeline()
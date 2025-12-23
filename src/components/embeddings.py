""" Embeddings component for the medical RAG chatbot. """

from langchain_huggingface import HuggingFaceEmbeddings
from src.common.custom_exception import CustomException
from src.common.logger import get_logger
from src.config.config import EMBEDDING_MODEL_NAME

logger = get_logger(__name__)

def get_embeddings():
    try:
        logger.info("Loading embeddings model...")
        embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
        logger.info("Embeddings model loaded successfully.")
        return embedding_model

    except Exception as e:
        logger.error(f"Error loading embeddings model: {e}")
        raise CustomException(f"Error loading embeddings model: {e}")
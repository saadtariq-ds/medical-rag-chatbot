""" LLM setup component for the medical RAG chatbot. """

from langchain_groq import ChatGroq
from src.config.config import LLM_MODEL, GROQ_API_KEY
from src.common.custom_exception import CustomException
from src.common.logger import get_logger


logger = get_logger(__name__)

def load_llm(model_name: str=LLM_MODEL, groq_api_key: str=GROQ_API_KEY):
    try:
        logger.info("Loading LLM from GROQ...")
        llm = ChatGroq(
            model_name=model_name,
            groq_api_key=groq_api_key,
            temperature=0.3,
            max_tokens=256
        )

        logger.info("LLM loaded successfully.")
        return llm

    except Exception as e:
        logger.error(f"Error loading LLM: {e}")
        raise CustomException(f"Error loading LLM: {e}")
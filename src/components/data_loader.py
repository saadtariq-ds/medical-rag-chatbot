""" Data loader component for the medical RAG chatbot. """

import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.common.logger import get_logger
from src.common.custom_exception import CustomException
from src.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)


def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException(f"Data path {DATA_PATH} does not exist.")
        
        logger.info(f"Loading PDF files from directory: {DATA_PATH}")
        loader = DirectoryLoader(path=DATA_PATH, glob="**/*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            logger.info("No PDF documents found.")
            raise CustomException("No PDF documents found in the specified directory.")
        logger.info(f"Loaded {len(documents)} documents from PDF files.")

        return documents

    except Exception as e:
        logger.error(f"Error loading PDF files: {e}")
        raise CustomException(f"Error loading PDF files: {e}")
    
def split_documents(documents):
    try:
        if not documents:
            raise CustomException("No documents provided for splitting.")
        
        logger.info("Splitting documents into chunks.")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        text_chunks = text_splitter.split_documents(documents)
        logger.info(f"Split documents into {len(text_chunks)} chunks.")
        return text_chunks

    except Exception as e:
        logger.error(f"Error splitting documents: {e}")
        raise CustomException(f"Error splitting documents: {e}")
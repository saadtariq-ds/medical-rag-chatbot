""" Retriever component for fetching relevant documents. """

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate
from src.components.vector_store import load_vector_store
from src.components.llm_setup import load_llm
from src.common.custom_exception import CustomException
from src.common.logger import get_logger
from src.config.prompts import MEDICAL_QA_PROMPT

logger = get_logger(__name__)


def set_custom_prompt():
    return PromptTemplate(
        template=MEDICAL_QA_PROMPT, input_variables=["context" , "question"]
    )

def create_qa_chain():
    try:
        logger.info("Loading vector store for retriever...")
        vector_store = load_vector_store()

        if vector_store is None:
            logger.error(f"Vector store does not exist:")
            raise CustomException(f"Vector store does not exist")
        
        llm = load_llm()

        if llm is None:
            logger.error(f"LLM not loaded")
            raise CustomException(f"LLM not loaded")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 1}),
            return_source_documents=False,
            chain_type_kwargs={"prompt": set_custom_prompt()},
        )
        logger.info("QA chain created successfully.")
        return qa_chain
    
    except Exception as e:
        logger.error(f"Error creating QA chain: {e}")
        raise CustomException(f"Error creating QA chain: {e}")
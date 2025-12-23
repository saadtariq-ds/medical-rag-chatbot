""" Prompt templates for the medical RAG chatbot. """

MEDICAL_QA_PROMPT = """ Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""
# app/services/vector_store.py

import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from app.core.config import CHROMA_DB_DIR

def create_or_load_vectorstore(docs):
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    vectordb.persist()
    return vectordb

def load_existing_vectorstore():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings
    )
    return vectordb
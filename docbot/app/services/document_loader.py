# app/services/document_loader.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def load_and_split_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    # ✅ Ensure all chunks are Document objects
    valid_docs = []
    for chunk in chunks:
        if isinstance(chunk, dict):
            valid_docs.append(Document(page_content=chunk["page_content"], metadata=chunk.get("metadata", {})))
        else:
            valid_docs.append(chunk)

    return valid_docs

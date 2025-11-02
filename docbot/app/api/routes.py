from fastapi import APIRouter, UploadFile, Form
from app.services.document_loader import load_and_split_pdf
from app.services.vector_store import create_or_load_vectorstore, load_existing_vectorstore
from app.services.qa_chain import build_qa_chain
import os

router = APIRouter()

@router.post("/upload")
async def upload_doc(file: UploadFile):
    os.makedirs("./data/sample_docs", exist_ok=True)
    file_path = f"./data/sample_docs/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    docs = load_and_split_pdf(file_path)
    vectordb = create_or_load_vectorstore(docs)
    return {"message": f"{file.filename} processed and stored successfully"}

@router.post("/ask")
async def ask_question(question: str = Form(...)):
    vectordb = load_existing_vectorstore()
    qa_chain = build_qa_chain(vectordb)
    response = qa_chain.run(question)
    # For RetrievalQA the return structure differs; handle common cases
    if isinstance(response, dict):
        answer = response.get("result") or response.get("answer") or str(response)
    else:
        answer = str(response)
    return {"answer": answer}

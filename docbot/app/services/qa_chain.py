from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def build_qa_chain(vectordb):
    # model_name can be changed to a model you have access to
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return qa

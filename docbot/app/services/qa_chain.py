# app/services/qa_chain.py

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

def build_qa_chain(vectorstore):
    """Builds a Q&A chain using LangChain 0.3.x Runnable pipeline"""
    
    # Convert vector store to retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Define the LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # Define the prompt template
    prompt = ChatPromptTemplate.from_template("""
    You are an expert assistant. Use the following context to answer the question.
    If you don't know the answer, say "I’m not sure, please provide more details."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """)

    # Build the chain using Runnable syntax
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return chain

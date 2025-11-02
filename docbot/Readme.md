# gamo_ai_hub

# DocBot - Basic (FastAPI + LangChain + OpenAI + Chroma)

This is a minimal working example of a Document Q&A chatbot using FastAPI, LangChain, OpenAI, and Chroma for vector storage.

## Structure

```
docbot_basic/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   ├── config.py
│   ├── services/
│   │   ├── document_loader.py
│   │   ├── vector_store.py
│   │   └── qa_chain.py
│   └── requirements.txt
├── data/
│   └── sample_docs/   # put sample PDFs here
└── .env.example
```

## Quick start

1. Create & activate a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate   # windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   python.exe -m pip install --upgrade pip
   pip install python-multipart
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`.
4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Open Swagger UI: http://127.0.0.1:8000/docs

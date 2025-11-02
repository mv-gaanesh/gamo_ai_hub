from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="DocBot - LangChain + FastAPI (Basic)")

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to DocBot! Upload a document and ask questions via /api endpoints."}

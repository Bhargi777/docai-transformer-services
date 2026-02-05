from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# Add root directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import models from services
# We import them here so that Vercel loads them in the serverless function
try:
    from services.summarization.app.model import summarizer_instance
    from services.question_answering.app.model import qa_instance
except ImportError as e:
    print(f"Import error: {e}")
    summarizer_instance = None
    qa_instance = None

app = FastAPI(title="DocAI Unified Service")

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 50

class QARequest(BaseModel):
    question: str
    context: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to DocAI Transformer Services",
        "endpoints": {
            "summarize": "/summarize",
            "qa": "/answer",
            "health": "/health"
        }
    }

@app.post("/summarize")
async def summarize(request: SummarizeRequest):
    if not summarizer_instance:
        raise HTTPException(status_code=500, detail="Summarization model not loaded")
    try:
        summary_text = summarizer_instance.summarize(
            request.text, 
            max_length=request.max_length, 
            min_length=request.min_length
        )
        return {"summary": summary_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/answer")
async def answer(request: QARequest):
    if not qa_instance:
        raise HTTPException(status_code=500, detail="QA model not loaded")
    try:
        answer_text = qa_instance.answer(
            request.question, 
            request.context
        )
        return {"answer": answer_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

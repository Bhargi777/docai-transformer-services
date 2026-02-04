from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import qa_instance

app = FastAPI(title="Question Answering Service")

class QARequest(BaseModel):
    question: str
    context: str

class QAResponse(BaseModel):
    answer: str

@app.post("/answer", response_model=QAResponse)
async def answer(request: QARequest):
    try:
        answer_text = qa_instance.answer(
            request.question, 
            request.context
        )
        return QAResponse(answer=answer_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import summarizer_instance

app = FastAPI(title="Document Summarization Service")

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 50

class SummarizeResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    try:
        summary_text = summarizer_instance.summarize(
            request.text, 
            max_length=request.max_length, 
            min_length=request.min_length
        )
        return SummarizeResponse(summary=summary_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

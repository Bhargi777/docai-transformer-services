# DocAI Transformer Services

Modular RESTful microservices for document summarization and question answering using transformer models.

## Services

1.  **Summarization Service**: Summarizes documents using pre-trained transformer models (e.g., BART, T5).
2.  **Question Answering (QA) Service**: Answers questions based on provided document context using BERT-based models.

## Tech Stack

-   **Language**: Python 3.9+
-   **Framework**: FastAPI
-   **AI Libs**: Hugging Face Transformers, PyTorch
-   **Containerization**: Docker, Docker Compose

## Getting Started

### Prerequisites

-   Docker and Docker Compose

### Running with Docker

```bash
docker-compose up --build
```

### Running Locally (Alternative)

If you don't have Docker installed, you can run the services using a Python virtual environment:

1. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r services/summarization/requirements.txt -r services/question_answering/requirements.txt
   ```

3. **Start the services**:
   * **Summarization**: `cd services/summarization && uvicorn app.main:app --port 8001`
   * **QA**: `cd services/question_answering && uvicorn app.main:app --port 8002`

4. **Test the services**:
   ```bash
   python test_services.py
   ```

### Deployment to Vercel

This project includes a `vercel.json` and a unified entry point in `api/index.py` for easy deployment to Vercel.

**Note on Vercel Limitations:**
- **Model Size**: Transformer models (like BART and BERT) are very large. Vercel Serverless Functions have a 250MB size limit. You may need to use smaller models (e.g., `distilbert`, `tiny-bert`) or external APIs (Hugging Face Inference API) for production.
- **Timeouts**: Model inference can exceed Vercel's execution time limits (10-60s).
- **Memory**: Ensure your Vercel plan supports the memory required for loading these models.

To deploy:
1. Push to GitHub.
2. Connect your repository to Vercel.
3. Vercel will automatically detect the configuration and deploy.

### API Endpoints

- **Summarization**: `POST /summarize` (or `POST http://localhost:8001/summarize` locally)
- **Question Answering**: `POST /answer` (or `POST http://localhost:8002/answer` locally)
- **Health**: `GET /health`

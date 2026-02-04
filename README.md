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

### Running the Services

```bash
docker-compose up --build
```

### API Endpoints

-   **Summarization**: `POST http://localhost:8001/summarize`
-   **Question Answering**: `POST http://localhost:8002/answer`

import os
import requests
from transformers import pipeline

class QuestionAnswering:
    def __init__(self, model_name="distilbert-base-cased-distilled-squad"):
        self.model_name = model_name
        self.qa_pipeline = None
        self.api_key = os.getenv("HUGGINGFACE_API_KEY")
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"

    def _load_model(self):
        if self.qa_pipeline is None and not self.api_key:
            print(f"Loading local QA model: {self.model_name}")
            self.qa_pipeline = pipeline("question-answering", model=self.model_name)

    def answer(self, question, context):
        if not question or not context:
            return ""

        if self.api_key:
            print(f"Using Hugging Face Inference API for QA ({self.model_name})")
            headers = {"Authorization": f"Bearer {self.api_key}"}
            payload = {
                "inputs": {
                    "question": question,
                    "context": context
                }
            }
            response = requests.post(self.api_url, headers=headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, dict) and 'answer' in result:
                    return result['answer']
            print(f"API Error: {response.text}")
            # Fallback to local if API fails and we are local

        self._load_model()
        if self.qa_pipeline:
            result = self.qa_pipeline(question=question, context=context)
            return result['answer']
        return "Error: Could not perform QA (no API key and local model failed to load)"

qa_instance = QuestionAnswering()


        
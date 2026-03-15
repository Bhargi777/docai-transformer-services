import os
import requests
from transformers import pipeline

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.model_name = model_name
        self.summarizer = None
        self.api_key = os.getenv("HUGGINGFACE_API_KEY")
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"

    def _load_model(self):
        if self.summarizer is None and not self.api_key:
            print(f"Loading local summarization model: {self.model_name}")
            self.summarizer = pipeline("summarization", model=self.model_name)

    def summarize(self, text, max_length=130, min_length=30):
        if not text:
            return ""

        if self.api_key:
            print(f"Using Hugging Face Inference API for summarization ({self.model_name})")
            headers = {"Authorization": f"Bearer {self.api_key}"}
            payload = {
                "inputs": text,
                "parameters": {"max_length": max_length, "min_length": min_length, "do_sample": False}
            }
            response = requests.post(self.api_url, headers=headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('summary_text', "")
            print(f"API Error: {response.text}")
            # Fallback to local if API fails and we are local
            
        self._load_model()
        if self.summarizer:
            summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]['summary_text']
        return "Error: Could not perform summarization (no API key and local model failed to load)"

summarizer_instance = Summarizer()



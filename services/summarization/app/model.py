from transformers import pipeline

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=130, min_length=30):
        if not text:
            return ""
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']

summarizer_instance = Summarizer()

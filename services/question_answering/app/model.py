from transformers import pipeline

class QuestionAnswering:
    def __init__(self, model_name="distilbert-base-cased-distilled-squad"):
        self.qa_pipeline = pipeline("question-answering", model=model_name)

    def answer(self, question, context):
        if not question or not context:
            return ""
        result = self.qa_pipeline(question=question, context=context)
        return result['answer']

qa_instance = QuestionAnswering()

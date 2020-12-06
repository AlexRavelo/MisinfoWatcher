from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from typing import List

class NamedEntityModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        self.model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")     
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)
        self.min_percent = 0.98

    def predict(self, text: str) -> List[str]:
        print("Inside of NER predict function")
        ner_results = self.nlp(text)
        words = []
        for entity in ner_results:
            if entity['score'] > self.min_percent and len(entity['word']) > 1 and '#' not in entity['word']:
                words.append(entity['word'])

        return list(set(words))

ner_model = NamedEntityModel()

# Ensures a singleton
def get_ner_model():
    return ner_model
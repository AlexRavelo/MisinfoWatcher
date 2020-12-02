from typing import Dict, List
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from .model import get_model, Model
from .ner_model import get_ner_model, NamedEntityModel
from .article_scraper import scrapeArticle
app = FastAPI()

class ClassifierRequest(BaseModel):
    url: str

class ClassifierResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float
    message: str
class NamedEntityResponse(BaseModel):
    entities: List[str]
    message: str


@app.post("/predictTitle")
def predictTitle(request: ClassifierRequest, model: Model = Depends(get_model)):
    try:
        title, text = scrapeArticle(request.url)
        sentiment, confidence, probabilities = model.predict(title)
        return ClassifierResponse(
        sentiment=sentiment, confidence=confidence, probabilities=probabilities, message="Success!"
    )
    except Exception as e:
        return ClassifierResponse(
        sentiment="null", confidence=0.0, probabilities={"null": 0.0}, message=f"Error scraping article: {e}"
    )
    
@app.post("/predictArticle", response_model=ClassifierResponse)
def predictArticle(request: ClassifierRequest, model: Model = Depends(get_model)):
    try:
        title, text = scrapeArticle(request.url)
        sentiment, confidence, probabilities = model.predict(text)
        return ClassifierResponse(
        sentiment=sentiment, confidence=confidence, probabilities=probabilities, message="Success!"
    )
    except Exception as e:
        return ClassifierResponse(
        sentiment="null", confidence=0.0, probabilities={"null": 0.0}, message=f"Error scraping article: {e}"
    )

@app.post("/grabEntities", response_model=NamedEntityResponse)
def grabEntities(request: NamedEntityResponse, model: NamedEntityModel = Depends(get_ner_model)):
    try:
        title, text = scrapeArticle(request.url)
        entities = model.predict(text)
        return NamedEntityResponse(
        entities=entities, message="Success!"
    )
    except Exception as e:
        return ClassifierResponse(
        sentiment="null", confidence=0.0, probabilities={"null": 0.0}, message=f"Error scraping article: {e}"
    )
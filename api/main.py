from typing import Dict
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from .model import get_model, Model
from .article_scraper import scrapeArticle
app = FastAPI()

class ClassifierRequest(BaseModel):
    url: str

class ClassifierResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float
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
    
    

# Dependency Injection thanks to FastAPI
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
    
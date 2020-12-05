from typing import Dict, List
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from .model import get_model, Model
from .ner_model import get_ner_model, NamedEntityModel
from fastapi.middleware.cors import CORSMiddleware
from .article_scraper import scrapeArticle


app = FastAPI()

# add our app middleware
origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

class MisinfoWatcherResponse(BaseModel):
    title_sentiment: str
    title_confidence: float
    article_sentiment: str
    article_confidence: float
    entities: List[str]

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
def grabEntities(request: ClassifierRequest, model: NamedEntityModel = Depends(get_ner_model)):
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

@app.post("/predict", response_model=MisinfoWatcherResponse)
def grabEntities(request: ClassifierRequest, article_model: Model = Depends(get_model), ner_model: NamedEntityModel = Depends(get_ner_model)):
    messages = []

    try:
        title, text = scrapeArticle(request.url)
        print("Success in scraping article!")
    except Exception as e:
        messages.append(f"Error scraping article: {e}")
        print(f"Error scraping article: {e}")
        return None # TODO


    try:
        entities = ner_model.predict(text)
        messages.append(f"Success in predicting entites: {entities}")
        print(f"Success in predicting entites: {entities}")
    except Exception as e:
        entities = ["None"]
        print(f"Error in predicting entites: {e}")
        messages.append(f"Error in predicting entites: {e}")

    try:
        text_sentiment, text_confidence, _ = article_model.predict(text)
        messages.append("Success in predicting article sentiment")
        print("Success in predicting article sentiment")
    except Exception as e:
        text_sentiment = "Unable to predict"
        text_confidence = 0.0
        print(f"Error in predicting article sentiment: {e}")
        messages.append(f"Error in predicting article sentiment: {e}")


    return MisinfoWatcherResponse(
        title_sentiment="foo",
        title_confidence=0.0,
        article_sentiment=str(text_sentiment),
        article_confidence=float(text_confidence),
        entities=entities
    )

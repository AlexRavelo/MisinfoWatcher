import requests
import urllib
import time
from typing import Tuple
from newspaper import Article

def scrapeArticle(url) -> Tuple[str, str]:
    # nabbing the article
    article = Article(url)
    article.download()
    article.html
    article.parse()
    
    # nabbing both the text and the title
    article_text = article.text
    title_text = article.title
    
    return title_text, article_text
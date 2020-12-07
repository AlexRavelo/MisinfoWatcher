import requests
import urllib
import time
from typing import Tuple
from newspaper import Article
<<<<<<< Updated upstream

def scrapeArticle(url) -> Tuple[str, str]:
=======
def scrapeArticle(url: str) -> Tuple[str, str]:
	
>>>>>>> Stashed changes
    # nabbing the article
    article = Article(url)
    article.download()
    article.html
    article.parse()
<<<<<<< Updated upstream
    
    # nabbing both the text and the title
    article_text = article.text
    title_text = article.title
    
    return title_text, article_text
=======

    # nabbing both the text and the title
    article_text = article.text
    title_text = article.title

	return title_text, article_text
>>>>>>> Stashed changes

import requests
import urllib
import time
from typing import Tuple
from bs4 import BeautifulSoup

def scrapeArticle(url: str) -> Tuple[str, str]:
	
	# Connect to the URL passed into the function
	response = requests.get(url)

	# Parse HTML as a BeautifulSoup object
	soup = BeautifulSoup(response.text, "html.parser")

	# Nabbing the title and page text
	article_text = soup.get_text()

	return article_text
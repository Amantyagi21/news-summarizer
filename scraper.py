import requests
from bs4 import BeautifulSoup

def news_lao(url="https://feeds.feedburner.com/ndtvnews-top-stories"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    
    articles = []
    for item in soup.find_all("item")[:10]:
        articles.append({
            "title": item.title.text,
            "description": item.description.text
        })
    return articles

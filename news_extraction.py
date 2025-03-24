import requests
from bs4 import BeautifulSoup
import requests
import json

API_KEY = "76c8e8525c094e39a65b59d0c5a8c4e8" 
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_news_articles(company, max_articles=7):
    params = {
        "q": company,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": max_articles,
        "apiKey": API_KEY,
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if "articles" not in data:
        return []  # Return empty if no articles are found

    articles = []
    for article in data["articles"][:max_articles]:
        articles.append({
            "title": article.get("title", "No Title"),
            "content": article.get("description", "No Content Available"),
            "url": article.get("url", "#"),
            "topics": [],  # Topics will be generated later
        })

    return articles

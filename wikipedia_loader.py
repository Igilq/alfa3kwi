import requests
from pyscript import Element
import asyncio

async def fetch_wikipedia_article():
    url = "https://pl.wikipedia.org/api/rest_v1/page/summary/Alfa_Romeo_164"
    response = await asyncio.to_thread(requests.get, url)
    data = response.json()

    article_content = f"<h2>{data['title']}</h2><p>{data['extract']}</p>"

    article_element = Element("articleContent")
    article_element.write(article_content)

def load_article(_):
    asyncio.ensure_future(fetch_wikipedia_article())
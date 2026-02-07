import requests
from bs4 import BeautifulSoup

WIKI_PREFIX = "https://en.wikipedia.org/wiki/"

def validate_wikipedia_url(url: str):
    return url.startswith(WIKI_PREFIX)

def scrape_wikipedia(url: str):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers, timeout=20)


    response.raise_for_status()

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1").get_text(strip=True)

    paragraphs = soup.select("p")
    content = " ".join(p.get_text(" ", strip=True) for p in paragraphs)
    content = content[:12000]

    summary = " ".join(p.get_text(" ", strip=True) for p in paragraphs[:3])
    summary = summary[:800]

    sections = [
        h.get_text(" ", strip=True)
        for h in soup.select("#mw-content-text h2 .mw-headline")
    ]

    return {
        "url": url,
        "title": title,
        "summary": summary,
        "sections": sections,
        "content": content,
        "raw_html": html
    }

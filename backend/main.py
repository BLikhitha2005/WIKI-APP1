from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .schemas import GenerateRequest
from .scraper import scrape_wikipedia, validate_wikipedia_url
from .llm import generate_quiz_and_entities, generate_related_topics
from .crud import get_by_url, create_record, list_records, get_by_id


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Wiki Quiz Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate-quiz")
def generate_quiz(req: GenerateRequest, db: Session = Depends(get_db)):
    if not validate_wikipedia_url(req.url):
        raise HTTPException(status_code=400, detail="Invalid Wikipedia URL")

    cached = get_by_url(db, req.url)
    if cached:
        return cached

    article = scrape_wikipedia(req.url)

    quiz_data = generate_quiz_and_entities(article["content"])
    topics_data = generate_related_topics(article["title"], article["summary"])

    payload = {
        "url": article["url"],
        "title": article["title"],
        "summary": article["summary"],
        "key_entities": quiz_data.get("key_entities"),
        "sections": article["sections"],
        "quiz": quiz_data.get("quiz"),
        "related_topics": topics_data.get("related_topics"),
        "raw_html": article["raw_html"]
    }

    return create_record(db, payload)

@app.get("/history")
def history(db: Session = Depends(get_db)):
    return list_records(db)

@app.get("/history/{quiz_id}")
def history_detail(quiz_id: int, db: Session = Depends(get_db)):
    quiz = get_by_id(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Not found")
    return quiz

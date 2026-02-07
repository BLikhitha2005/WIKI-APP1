from sqlalchemy import Column, Integer, String, DateTime, JSON, Text, func
from .database import Base

class QuizRecord(Base):
    __tablename__ = "quiz_records"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    summary = Column(Text)

    key_entities = Column(JSON)
    sections = Column(JSON)
    quiz = Column(JSON)
    related_topics = Column(JSON)

    raw_html = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())









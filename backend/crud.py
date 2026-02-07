from sqlalchemy.orm import Session
from .models import QuizRecord


def get_by_url(db: Session, url: str):
    return db.query(QuizRecord).filter(QuizRecord.url == url).first()


def create_record(db: Session, payload: dict):
    record = QuizRecord(**payload)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def list_records(db: Session):
    return db.query(QuizRecord).order_by(QuizRecord.created_at.desc()).all()


def get_by_id(db: Session, record_id: int):
    return db.query(QuizRecord).filter(QuizRecord.id == record_id).first()

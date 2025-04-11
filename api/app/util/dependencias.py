from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import sessionmaker
from app.util.bd import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
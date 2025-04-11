from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.util.bd import Base

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(50), nullable=False)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
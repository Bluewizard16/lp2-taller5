from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from app.models.users import User

class Post(Base):
    __tablename__ = "publicaciones"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    contenido = Column(String, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), index=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
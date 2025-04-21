from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Comment(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True)
    comentario = Column(String, nullable=False)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
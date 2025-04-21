from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CommentBase(BaseModel):
    comentario: str

class CommentCreate(CommentBase):
    id_publicacion: int

class CommentUpdate(CommentBase):
    comentario: str | None = None

class CommentResponse(CommentBase):
    id: int
    id_publicacion: int
    id_usuario: int
    fecha_creacion: datetime

    model_config = ConfigDict(from_attributes=True)
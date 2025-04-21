from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PostBase(BaseModel):
    titulo: str
    contenido: str
    url_imagen: str | None = None

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    titulo: str | None = None
    contenido: str | None = None
    url_imagen: str | None = None

class PostResponse(PostBase):
    id: int
    id_usuario: int
    fecha_creacion: datetime

    model_config = ConfigDict(from_attributes=True)
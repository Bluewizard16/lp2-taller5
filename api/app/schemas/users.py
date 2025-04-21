from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    usuario: str
    nombre: str
    email: str

class UserResponse(UserBase):
    id: int
    fecha_creacion: datetime
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    usuario: Optional[str] = None
    nombre: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# User login request schema
class USR_LOG_REQ(BaseModel):
    email: str
    password: str

# User base schema
class USR(BaseModel):
    usuario: str
    nombre: str
    email: str

# User response schema with additional fields
class USR_RES(USR):
    id: int
    fecha_creacion: datetime
    model_config = ConfigDict(from_attributes=True)

# User registration schema
class USR_NW(USR):
    password: str

# User update schema
class USR_UP(BaseModel):
    usuario: Optional[str] = None
    nombre: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
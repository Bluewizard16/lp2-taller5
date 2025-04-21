from pydantic import BaseModel, EmailStr
from app.schemas.users import UserResponse
from datetime import datetime

class LoginRequest(BaseModel):
    email: str
    password: str

# class UserCreate(BaseModel):
#     usuario: str
#     nombre: str
#     email: str
#     password: str
#     fecha_creacion: datetime = datetime.utcnow()

class LoginResponse(BaseModel):
    user: UserResponse
    access_token: str
    token_type: str = "bearer"
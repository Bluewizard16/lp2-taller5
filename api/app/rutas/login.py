from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.model.login import User
from app.schema.login import USR, USR_RES, USR_NW, USR_UP, USR_LOG_REQ
from app.util.dependencias import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/login", response_model=USR_RES)
async def login_user(request: USR_LOG_REQ, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or user.password != request.password:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    return user


@router.post("/register", response_model=USR_RES)
async def register_user(user: USR_NW, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
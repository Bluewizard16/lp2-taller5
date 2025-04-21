from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserResponse, UserCreate, UserUpdate
from datetime import datetime
from app.deps import get_db, get_current_user
from app.utils.auth import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserResponse] | UserResponse)
def get_users(
    user_id: int = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if user_id:
        user = db.query(User).get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user
    return db.query(User).all()

@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    db_user = User(
        usuario=user.usuario,
        nombre=user.nombre,
        email=user.email,
        password= get_password_hash(user.password),
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_user = db.query(User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_user = db.query(User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(db_user)
    db.commit()
    return {"message": "Usuario eliminado"}
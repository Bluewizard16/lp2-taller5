from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, LoginResponse
from app.models.users import User
from app.utils.auth import create_access_token, verify_password, get_password_hash
from app.deps import get_db
from app.schemas.auth import LoginResponse, LoginRequest

router = APIRouter(tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = create_access_token(data={"sub": str(user.id)})
    return LoginResponse(user=user, access_token=token, token_type="bearer")


@router.post("/login-form", response_model=LoginResponse)
def login_form(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.usuario == form_data.username)  # Cambiado de email a usuario
        .first()
    )
    if not user:
        print("Usuario no encontrado:", form_data.username)
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if not verify_password(form_data.password, user.password):
        print("Contraseña incorrecta para el usuario:", form_data.username)
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer", "user": user}

# @router.post("/register", response_model=UserResponse)
# def register(user_data: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.email == user_data.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="El correo ya está registrado")

#     hashed_password = get_password_hash(user_data.password)
#     user_data.password = hashed_password
#     new_user = User(
#         usuario=user_data.usuario,
#         email=user_data.email,
#         password=user_data.password,
#         nombre=user_data.nombre,
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return UserResponse(
#         id=new_user.id,
#         usuario=new_user.usuario,
#         email=new_user.email,
#         nombre=new_user.nombre,
#         fecha_creacion=new_user.fecha_creacion
#     )
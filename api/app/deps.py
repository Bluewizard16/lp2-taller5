from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.utils.auth import decode_token
from app.models.users import User

# OAuth2 esquema de autenticación que permite a los usuarios
# obtener un token de acceso para acceder a recursos 
# protegidos en una API. El token se obtiene al enviar 
# las credenciales del usuario (nombre de usuario y contraseña) 
# a un endpoint específico (en este caso, "login").
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") 

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependencia para obtener el usuario actual a partir del token
# de acceso. Se decodifica el token y se busca el usuario en la base de datos.
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    user = db.query(User).get(int(user_id))
    # Si el usuario no existe, se lanza una excepción HTTP 404
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
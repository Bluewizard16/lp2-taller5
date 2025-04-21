from fastapi import FastAPI
import uvicorn
from app.routes import auth, users, posts, comments
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Blog",
    description="API para un blog con FastAPI y SQLAlchemy",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto por los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye las rutas de autenticación
app.include_router(auth.router, prefix="/auth", tags=["auth"])
# Incluye las rutas de usuarios
app.include_router(users.router, prefix="/users", tags=["users"])
# Incluye las rutas de publicaciones
app.include_router(posts.router, prefix="/posts", tags=["posts"])
# # Incluye las rutas de comentarios
app.include_router(comments.router, prefix="/comments", tags=["comments"])


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
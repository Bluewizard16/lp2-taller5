from fastapi import FastAPI
import uvicorn
from app.rutas import login

app = FastAPI()

app.include_router(login.router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
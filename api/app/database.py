from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargamos el archivo .env para obtener la URL de la base de datos
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# Creamos la conexión a la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creamos una clase base para nuestros modelos
Base = declarative_base()
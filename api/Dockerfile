# Usa la imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /api

# Copia los archivos de dependencias (requirements.txt) al directorio de trabajo
COPY requirements.txt ./

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY ./app .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Define el comando para ejecutar la aplicación
CMD ["python","-m", "app.main"]
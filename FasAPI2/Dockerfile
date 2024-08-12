FROM python:3.12-slim

# Desactivar la verificación de versión de pip y configurar Python sin búfer
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Crear un entorno virtual y instalar las dependencias
RUN python -m venv venv \
    && /app/venv/bin/pip install --upgrade pip \
    && /app/venv/bin/pip install -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY src /app/src

# Exponer el puerto en el que la aplicación estará corriendo
EXPOSE 8000

# Agrega una verificación para asegurar que uvicorn esté presente
RUN ls -la /app/venv/bin/uvicorn

# Comando para ejecutar la aplicación usando el ejecutable de uvicorn en el entorno virtual

CMD ["/app/venv/bin/uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]


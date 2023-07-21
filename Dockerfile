# Imagen base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Directorio de trabajo
WORKDIR /app

# Copia de archivos al contenedor
COPY requirements.txt .

# Instalación de dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia de archivos al contenedor
COPY . .

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
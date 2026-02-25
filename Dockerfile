FROM python:3.10-slim

# Carpeta de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear carpetas necesarias
RUN mkdir -p data/raw data/processed

# Comando principal
CMD ["python", "-m", "src.pipeline.run_pipeline"]
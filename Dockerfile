# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los requisitos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]  # Cambia esto según tu archivo principal
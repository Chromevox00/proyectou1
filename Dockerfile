# Materia: Automatización de Infraestructura Digital II
# Alumna: Samantha Carolina Ramírez Montiel
# Profesor: Froylan Alonso Pérez Alanís

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
EXPOSE 5000
CMD ["python", "app.py"]

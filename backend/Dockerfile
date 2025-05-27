# Usa un'immagine base python
FROM python:3.9-slim

# Setta la working directory dentro il container
WORKDIR /app

# Copia requirements e installa dipendenze
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del backend dentro /app
COPY . .

# Esponi la porta su cui gira il backend
EXPOSE 8000

# Comando di default
CMD ["uvicorn", "cardmarket_api.api:app", "--host", "0.0.0.0", "--port", "8000"]
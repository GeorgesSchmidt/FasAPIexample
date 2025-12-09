# Utilise une image Python officielle légère
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le projet
COPY . .

# Expose le port 8000
EXPOSE 8000

# Commande pour lancer l'app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

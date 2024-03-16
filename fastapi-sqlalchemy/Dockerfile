# Usa un'immagine di Python predefinita
FROM python:3.9

# Imposta il percorso di lavoro nell'immagine
WORKDIR /app

# Copia tutti i file nella cartella corrente nella directory di lavoro dell'immagine
COPY . .

# Installa Poetry
RUN pip install poetry

# Installa le dipendenze del progetto usando Poetry
RUN poetry install

# Avvia l'applicazione
CMD poetry run start



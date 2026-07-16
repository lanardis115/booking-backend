# 1. Usa l'immagine ufficiale di Node
FROM node:20-slim

# 2. Installa gli strumenti necessari a compilare librerie native (es. better-sqlite3)
RUN apt-get update && apt-get install -y \
    python3 \
    make \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 3. Imposta la cartella di lavoro
WORKDIR /app

# 4. Copia i file di configurazione delle librerie
COPY package*.json /app/

# 5. Installa le librerie JavaScript (usiamo --legacy-peer-deps per evitare blocchi di versioni)
RUN npm install --legacy-peer-deps

# 6. Copia tutto il resto del codice di BookingMIMO
COPY . /app/

# 7. Esponi la porta (es. 3000)
EXPOSE 3000

# 8. Avvia la nostra RestAPI
CMD ["node", "server.js"]
# Usa un'immagine base node
FROM node:18-alpine

# Setta la working directory dentro il container
WORKDIR /app

# Copia package.json e package-lock.json (se c'è)
COPY package*.json ./

# Installa le dipendenze
RUN npm install

# Copia il resto del frontend dentro /app
COPY . .

# Esponi la porta 3000 per React
EXPOSE 3000

# Comando di default per avviare il dev server
CMD ["npm", "start"]
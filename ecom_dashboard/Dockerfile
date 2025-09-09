FROM node:18-alpine

# Set working directory
WORKDIR /app

COPY package*.json ./

RUN npm install

# Copy rest of the app
COPY . .

EXPOSE 3000

# Run Next.js in development mode
CMD ["npm", "run", "dev"]

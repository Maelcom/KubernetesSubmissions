FROM node:26-alpine3.24
WORKDIR /usr/src/app
COPY package* ./
RUN npm ci
COPY . .
CMD ["npm", "start"]

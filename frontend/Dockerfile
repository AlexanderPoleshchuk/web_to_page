FROM node:16-alpine

WORKDIR /usr/src/frontend

COPY package.json ./

RUN npm install -g npm@8.6.0

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
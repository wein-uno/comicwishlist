# Need a docker file for each container
FROM node:14

WORKDIR /app

COPY ./frontend /app

RUN npm install

CMD ["npm", "start"]

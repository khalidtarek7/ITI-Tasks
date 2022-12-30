### Problem 1: Convert the created react app multi-stage docker image into compose format.
```bash
#Build Source Code Stage:

FROM node:alpine3.16 AS builder

WORKDIR /app

COPY package*json ./

RUN npm install

COPY . .

RUN npm run build

#Deploy Stage

FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 3000

ENTRYPOINT ["nginx","-g","daemon off;"]

sudo docker build -t my-reactapp:1.0 .
```
Docker Compose File:
```bash
#sudo docker run -it --name my-reactapp -p 8001:3000 my-reactapp:1.0
version: '3.8'
services:
  my-reactapp:
    container_name: my-reactapp
    image: my-reactapp:1.1
    ports:
      - "8001:80"

sudo docker compose up -d
```
-----------------------------------------------
### Problem 2: Python App
Building the image:
```bash
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "app.py"]
```
Docker Compose File:
```bash
#sudo docker run -it --name myredis redis:latest
#sudo docker run -it --name mypython-counter python-counter:1.0
version: '3'

services:

  redis:
    container_name: myredis
    image: redis:latest
    ports:
      - 6379
    # networks:
    #   - app-tier

  python_app:
    container_name: mypython-counter
    image: python-counter:1.1
      
    depends_on:
      - redis
    # networks:
    #   - app-tier
    # command:
    #   tail -f /dev/null
    stop_signal: SIGINT
    ports:
      - "8003:8000"
```

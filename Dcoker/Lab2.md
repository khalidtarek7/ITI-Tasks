### Problem 1
Nginx image:
```bash
FROM ubuntu:23.04
RUN apt-get update
RUN apt-get install nginx -y
COPY index.html /var/www/html/
ADD khalid.tar /var/www/html/
EXPOSE 80
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
sudo docker build -t mynginx:1.0 .
sudo docker run -it -d --name ngnixkhalid -p 8090:80 mynginx:1.0
```
-----------------------
### Problem 2
Reactapp Single Stage:
```bash
FROM node:16-alpine
WORKDIR /app
COPY . .
RUN npm ci
RUN npm run build
ENV NODE_ENV production
EXPOSE 3000
CMD [ "npx", "serve", "build" ]
sudo docker build -t reactapplication:1.0 .
sudo docker run -it -d -p 5000:3000 reactapplication:1.0
the image size is 592 MB
```
Reactapp multistage:
```bash
FROM node:15.4 as build 


WORKDIR /react-app


COPY package*.json .


RUN yarn install


COPY . .


RUN yarn run build


FROM nginx:1.19


COPY ./nginx/nginx.conf /etc/nginx/nginx.conf


COPY --from=build /react-app/build /usr/share/nginx/html

sudo docker build -t reactapplication:1.1 .

sudo docker run -it -d -p 8090:3000 reactapplication:1.1

the image size is 592 MB
```
-----------------------------
### Problem 3:
Docker Networks:
```bash
Bridge Network:
its the default private internal network, you should port map it to another port to be able to start in your browser.
Host Network:
its the network in which one container can listen on only one specific port.
None Network:
its a private network in which  the container is completely isolated.
Overlay Network:
its a network that can connect more than one docker host which are distant with a range of ip addresses.
```
---------------------------------
### Problem 4:
Create Network:
```bash
sudo docker network create khalid-bridge
sudo docker network ls
sudo docker run -it -d --name ubuntu1 ubuntu:latest
sudo docker network connect ubuntu1
sudo docker container run -it --name ubuntu3 --add-host web:172.17.0.4 ubuntu
sudo docker network connect khalid-bridge ubuntu3
sudo docker exec -ti ubuntu1 ping ubuntu3
```

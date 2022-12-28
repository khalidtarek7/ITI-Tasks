### Lab1 Problem 1
1. Run the Container:
```bash
sudo docker run hello-world
```
2. Check the status:
```bash
sudo docker ps -a
```
3. Start the stopped container:
```bash
sudo docker start 90ee (Container id)
```
4. Remove the container:
```bash
sudo docker rm 90ee
```
5. Remove the image:
```bash
sudo docker rmi feb5d
```
-----------
### Problem 2
1. Run container centos or ubuntu in an interactive mode:
```bash
sudo docker run -it ubuntu:22.04
```
2. Run the following command in the container echo docker :
```bash
echo docker
```
3. Open a bash shell in the container and touch a file named hello-docker:
```bash
touch hello-docker
```
4. Stop the container and remove it. Write your comment about the file hello-docker:
```bash
sudo docker stop 6acc
sudo docker rm 6acc
The file will be deleted
```
5. Remove all stopped containers:
```bash
sudo docker rm $(sudo docker ps --filter status=exited -q)
```
-----------
### Problem 3
1. Attach the volume:
```bash
sudo docker run -it -v volume1:/var/www/html --name apache httpd bash
echo khalid >> lab1.text
```
1. Attach the volume:
```bash
sudo docker run -it -v volume1:/var/www/html --name apache httpd bash
echo khalid >> lab1.text
```
2. Remove the container:
```bash
sudo docker container ls -a
```
3. Remove the container:
```bash
sudo docker rm d80
```
4. Run new container:
```bash
sudo docker run -it -v volume2:/usr/local/apache2/htdocs --name apache2 -p 9080:80  httpd
```
-------
### Problem 4

1. Commit the changes:
```bash
sudo docker commit 4b0 my_apache:1
```
2. Create docker file for Nginx:
```bash
touch Dockerfile
vim Dockerfile
write:
FROM nginx
 
 RUN apt-get update && apt-get upgrade -y
 
 COPY index.html /usr/share/nginx/html

 sudo docker build .
```
-------------------
### Problem 5

1. Mysql image:
```bash
sudo docker run -it -v volume3:/var/lib/mysql --name app-database -e MYSQL_ROOT_PASSWORD=P4sSw0rd0! -d mysql:latest
```
--------------------

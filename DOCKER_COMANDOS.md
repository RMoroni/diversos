# Introdução

# Comandos Docker
## Obter Informações
```
docker images
docker ps
docker ps -s # Size
docker port CONTAINER_ID
docker inspect IMAGE_ID
docker history IMAGE_ID
docker volume ls # lista volumes gerenciado pelo docker
docker network ls
```

## Construção e Execução
```
docker run -it IMAGE
docker run -P IMAGE
docker run -p HOST_PORT:CONTAINER_PORT IMAGE
docker run -it -v HOST_DIR:CONTAINER_DIR IMAGE COMMAND
docker run -it -v VOLUME:CONTAINER_DIR IMAGE COMMAND
docker run -it --mount type=bind,source=HOST_DIR,target=CONTAINER_DIR IMAGE COMMAND
docker run -it --mount type=source=VOLUME,target=CONTAINER_DIR IMAGE COMMAND
docker run -it --tmpfs=CONTAINER_DIR IMAGE COMMAND
docker exec -it CONTAINER_ID bash
docker-compose up
docker-compose -f docker-compose.yml up
docker volume create VOLUME
docker network create --driver bridge NOME_REDE_BRIDGE
docker run -it --name HOSTNAME --network NOME_REDE IMAGE COMMAND
```

## Remoção
```
docker container rm $(docker container ls -aq)
docker rmi $(docker images ls -aq) --force
docker builder prune # apenas o cache
docker system prune -a -f # PERIGO: apaga imagens e containers
```
## Outros
```
groupadd docker # cria grupo docker
usermod -aG docker $USER # adiciona usuário ao grupo do docker
newgrp docker # ativa as mudanças de grupo
docker login -u USER # loga no dockerhub, necessário para push
docker push IMAGE # sobe imagem para o dockerhub
```

# Comandos Dockerfile

## Básico
```
FROM IMAGE_NAME:VERSION # Ex: node:14, apache/airflow:latest
WORKDIR DIR
COPY HOST_DIR CONTAINER_DIR
ENV ENV_VAR=ENV_VALUE ENV_VAR2=ENV_VALUE2 ...
RUN COMMAND
ENTRYPOINT COMMAND
CMD COMMAND
```
Documentação: https://docs.docker.com/engine/reference/builder/

## RUN vs CMD vs ENTRYPOINT
O RUN é executado na construção da imagem, logo em um dockerfile é possível ter vários RUN para realizar os ajustes necessários (atualizar SO, instalar pacotes, etc). O CMD é executado assim que a imagem é executada, ou seja, não é executado durante a construção, por isso apenas um CMD é interpretado no dockerfile (se tiver dois, o último é o que vale). É o que equivalente a passar um comando via docker run. O ENTRYPOINT possui um comportamento bem similar ao CMD porém argumentos passados via docker run ou via CMD são direcionados como argumentos para o ENTRYPOINT, por isso deve-se tomar cuidado visto que isso pode causar comportamentos inesperados. Por isso é importante utilizar o ENTRYPOINT apenas quando o comando é estritamente necessário e não pode ser feito de outra forma, caso contrário é mais interessante utilizar o CMD que é mais flexivel.

## Bridge vs Host vs None
Bridge: utiliza outra rede para hospedar os containers
Host: utiliza a mesma interface de rede para hospedar os containers
None: não utiliza interface de rede

## Docker Compose Commands
```
docker-compose up -d
docker-compose down
docker-compose ps
```

## Docker Compose .yml
```
version: "3.9"
services:
    service_db_name:
        image: db_docker_image:version
        container_name: name
        networks:
            - docker_network_name

    service_app_name:
        image: image_name:version
        container_name: name
        networks:
            - docker_network_name
        ports:
            - host_port:container_port
        depends_on:
            - service_db_name

networks:
    docker_network_name:
        driver: driver # bridge, host, none

services:
  my-service:
    network_mode: host
```

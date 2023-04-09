## notes
up and down
cd examples/docker/qdrant/; docker-compose up -d
docker-compose -f examples/docker/qdrant/docker-compose.yaml up -d
cd examples/docker/qdrant/; docker-compose down
docker-compose -f examples/docker/qdrant/docker-compose.yaml down

https://docs.docker.com/storage/volumes/
docker volume inspect qdrant_qdrant-data
### minimal container to access the data in integrated terminal
docker run -it --rm -v qdrant_qdrant-data:/qdrant/storage busybox sh

## first go was this
1. 'poetry shell'
1. export the env variables
    1.1 DATASTORE=qdrant
    1.1 BEARER_TOKEN= from wsl_multi_root.chat.jwt_token
    1.1 OPENAI_API_KEY= from wsl_multi_root.chat.openai_api...
1. start qdrant datastore
    1.1 Docker Desktop
        1.1.1 open docker / containers
        1.1.1 start qdrant
    1.1 Command line (preferred as it uses the Docker Volume)
        1.1.1 docker run --rm --name=qdrant_tmp --hostname=3cdbfbc9d21d --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=TZ=Etc/UTC --env=RUN_MODE=production --workdir=/qdrant -p 6333:6333 -p 6334:6334 -v qdrant_qdrant-data:/qdrant/storage --restart=no --label='desktop.docker.io/wsl-distro=Ubuntu-20.04' --runtime=runc -d qdrant/qdrant:v1.0.3

1. 'poetry run start'


## for debugging
1. start qdrant datastore
1. run Debug configuration

## docker app with qdrant using a volume for persisting information
1. docker-compose -f examples/docker/qdrant/docker-compose.yaml up -d
# Richiede Docker

# Builda l'immagine docker
docker build --no-cache -t leocraco/aeroporti:v1 .

# Facciamo partire un container
CONTAINER_ID = $(docker run -d leocraco/aeroporti:v1)

# Copia del container su host
docker cp ${CONTAINER_ID}:"${WORKSPACE}" ./
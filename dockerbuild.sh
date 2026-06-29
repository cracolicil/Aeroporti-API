# Richiede Docker

# Builda l'immagine docker
docker build --no-cache -t leocraco/aeroporti:v1 .

# Facciamo partire un container per test
CONTAINER_ID=$(docker run -d leocraco/aeroporti:v1)

# Possibili test API

# Pulizia del container dopo averlo testato
docker rm -f ${CONTAINER_ID} || true

# Push dell'immagine su Registry
docker push leocraco/aeroporti:v1
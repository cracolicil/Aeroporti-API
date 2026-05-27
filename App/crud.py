import logging
from .database import aeroporti_db

logger = logging.getLogger(__name__)

def get_aeroporti(page: int, size: int):
    logger.info(f"Fetching airports page={page} size={size}")
    start = (page - 1) * size
    end = start + size
    return aeroporti_db[start:end]

def get_aeroporto(id: int):
    logger.info(f"Fetching airport with id:{id}")
    for airport in aeroporti_db:
        if airport["id"] == id:
            return airport

    logger.warning(f"Airport with id:{id} Not Found")
    return None
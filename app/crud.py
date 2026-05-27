import logging
from .database import aeroporti_db

logger = logging.getLogger(__name__)

def get_aeroporti(page: int, size: int):
    logger.info(f"Fetching airports page={page} size={size}")
    start = (page - 1) * size
    end = start + size
    if size > len(aeroporti_db):
        total = 1
    else:
        total = len(aeroporti_db) / size
    return {
        "page": page,
        "size": size,
        "total": total,
        "data": aeroporti_db[start:end]
    }

def get_aeroporto(id: int):
    logger.info(f"Fetching airport with id:{id}")
    for airport in aeroporti_db:
        if airport["id"] == id:
            return airport

    logger.warning(f"Airport with id:{id} Not Found")
    return None

def create_aeroporto(airport_data: dict):
    new_id = len(aeroporti_db) + 1
    new_airport = {"id": new_id, **airport_data}
    aeroporti_db.append(new_airport)
    logger.info(f"Airport created with id:{new_id}")
    return new_airport

def delete_aeroporto(id: int):
    airport = get_aeroporto(id)
    if not airport:
        return None
    logger.info(f"Airport with id:{id} successfully removed")
    return 0
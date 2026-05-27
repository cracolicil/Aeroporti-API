import logging
from .database import aeroporti_db

logger = logging.getLogger(__name__)

def get_aeroporti(page: int, size: int):
    logger.info(f"Fetching airports page={page} size={size}")
    start = (page - 1) * size
    end = start + size
    return aeroporti_db[start:end]
from fastapi import APIRouter, HTTPException
from typing import List
from .. import crud
from ..models import Aeroporto, AeroportoBase

router = APIRouter(prefix="/aeroporti", tags=["Aeroporti"])
@router.get("", response_model=List[Aeroporto])
def list_airports(page: int = 1, size = 10):
    return crud.get_aeroporti(page, size)
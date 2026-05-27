from fastapi import APIRouter, HTTPException
from typing import List
from .. import crud
from ..models import Aeroporto, AeroportoBase

router = APIRouter(prefix="/aeroporti", tags=["Aeroporti"])
@router.get("", response_model=List[Aeroporto])
def list_airports(page: int = 1, size = 10):
    return crud.get_aeroporti(page, size)

@router.get("/{airport_id}", response_model=Aeroporto)
def get_airport(airport_id: int):
    airport = crud.get_aeroporto(airport_id)
    if not airport:
        raise HTTPException(status_code=404, detail="Airport not found")
    return airport
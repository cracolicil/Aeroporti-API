from fastapi import APIRouter, HTTPException
from typing import List
from .. import crud
from ..models import Aeroporto, AeroportoBase

router = APIRouter(prefix="/aeroporti", tags=["Aeroporti"])
@router.get("", response_model=dict)
def list_airports(page: int = 1, size: int = 10):
    return crud.get_aeroporti(page, size)

@router.get("/{airport_id}", response_model=Aeroporto)
def get_airport(airport_id: int):
    airport = crud.get_aeroporto(airport_id)
    if not airport:
        raise HTTPException(status_code=404, detail="Airport not found")
    return airport

@router.post("", response_model=Aeroporto, status_code=201)
def create_airport(airport: AeroportoBase):
    return crud.create_aeroporto(airport.model_dump())

@router.delete("/{airport_id}", status_code=204)
def delete_airport(airport_id: int):
    airport = get_airport(airport_id)
    crud.delete_aeroporto(airport_id)
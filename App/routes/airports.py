from fastapi import APIRouter, HTTPException
from typing import List
from .. import crud
from ..models import Aeroporto, AeroportoBase

router = APIRouter(prefix="/aeroporti", tags=["Aeroporti"])
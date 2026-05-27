from pydantic import BaseModel, Field

class Aeroporto(BaseModel):
    id: int
    codice: str = Field(min_length=3, max_length=3)
    citta: str = Field(min_length=1)

class AeroportoBase(BaseModel):
    codice: str = Field(min_length=3, max_length=3)
    citta: str = Field(min_length=1)
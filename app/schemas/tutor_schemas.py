# veterinaria/schemas/tutor_schemas.py
from pydantic import BaseModel
from typing import List


class _PetBase(BaseModel):
    nome: str
    especie: str
    idade: int

class Pet(_PetBase):
    id: int
    
    class Config:
        from_attributes = True



class TutorBase(BaseModel):
    nome: str
    telefone: str

class TutorCreate(TutorBase):
    pass

class Tutor(TutorBase):
    id: int
    pets: List[Pet] = []

    class Config:
        from_attributes = True
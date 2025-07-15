from pydantic import BaseModel
from typing import List
from .tutor_schemas import Tutor


class _AtendimentoBase(BaseModel):
    id: int
    descricao: str
    
    class Config:
        from_attributes = True



class PetBase(BaseModel):
    nome: str
    especie: str
    idade: int

class PetCreate(PetBase):
    tutor_id: int

class Pet(PetBase):
    id: int
    tutor: Tutor 
    atendimentos: List[_AtendimentoBase] = []

    class Config:
        from_attributes = True
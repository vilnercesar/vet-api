
from pydantic import BaseModel
from datetime import datetime
from .pet_schemas import PetBase 
from .veterinario_schemas import VeterinarioBase 

class _Pet(PetBase):
    id: int
    class Config:
        from_attributes = True

class _Veterinario(VeterinarioBase):
    id: int
    class Config:
        from_attributes = True


class AtendimentoBase(BaseModel):
    descricao: str

class AtendimentoCreate(AtendimentoBase):
    pet_id: int
    veterinario_id: int

class Atendimento(AtendimentoBase):
    id: int
    data: datetime
    pet: _Pet
    veterinario: _Veterinario

    class Config:
        from_attributes = True
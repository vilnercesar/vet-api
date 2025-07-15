from pydantic import BaseModel
from typing import List
from datetime import datetime

class _AtendimentoBase(BaseModel):
    data: datetime
    descricao: str

class Atendimento(_AtendimentoBase):
    id: int
    
    class Config:
        from_attributes = True

class _ClinicaBase(BaseModel):
    nome: str
    cidade: str

class Clinica(_ClinicaBase):
    id: int

    class Config:
        from_attributes = True



class VeterinarioBase(BaseModel):
    nome: str
    especialidade: str


class VeterinarioCreate(VeterinarioBase):
    clinica_id: int


class Veterinario(VeterinarioBase):
    id: int
    clinica: Clinica
    atendimentos: List[Atendimento] = []

    class Config:
        from_attributes = True
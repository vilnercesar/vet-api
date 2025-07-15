from pydantic import BaseModel
from typing import List

# Schema para Veterinário
class _VeterinarioBase(BaseModel):
    nome: str
    especialidade: str

class Veterinario(_VeterinarioBase):
    id: int

    class Config:
        from_attributes = True 



# Schema base com os campos comuns
class ClinicaBase(BaseModel):
    nome: str
    cidade: str

# Schema para a criação de uma clínica (o que a API vai receber)
class ClinicaCreate(ClinicaBase):
    pass

# Schema para a resposta da API (o que a API vai enviar)
class Clinica(ClinicaBase):
    id: int
    veterinarios: List[Veterinario] = []

    class Config:
        from_attributes = True
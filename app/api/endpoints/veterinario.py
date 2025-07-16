from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import veterinario_service
from app.schemas import veterinario_schemas, atendimento_schemas

router = APIRouter(
    prefix="/veterinarios",
    tags=["Veterinários"]
)

@router.post("/", response_model=veterinario_schemas.Veterinario, status_code=status.HTTP_201_CREATED)
def create_veterinario(veterinario: veterinario_schemas.VeterinarioCreate, db: Session = Depends(get_db)):
    """
    Endpoint para cadastrar um novo veterinário.
    A camada de serviço já valida se a clínica associada existe.
    """
    service = veterinario_service.VeterinarioService(db)
    return service.create_veterinario(veterinario)

@router.get("/", response_model=List[veterinario_schemas.Veterinario])
def list_veterinarios(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os veterinários.
    """
    service = veterinario_service.VeterinarioService(db)
    return service.get_all_veterinarios()

@router.get("/{veterinario_id}/atendimentos", response_model=List[atendimento_schemas.Atendimento])
def get_veterinario_atendimentos(veterinario_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os atendimentos de um veterinário específico.
    """
    service = veterinario_service.VeterinarioService(db)
    
    if not service.get_veterinario_by_id(veterinario_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Veterinário não encontrado"
        )
        
    return service.get_atendimentos_by_veterinario_id(veterinario_id)
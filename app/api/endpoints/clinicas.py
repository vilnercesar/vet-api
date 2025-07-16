from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from ...database import get_db
from ...services import clinica_service
from ...schemas import clinica_schemas, veterinario_schemas


router = APIRouter(
    prefix="/clinicas",
    tags=["Clínicas"] 
)

@router.post("/", response_model=clinica_schemas.Clinica, status_code=status.HTTP_201_CREATED)
def create_clinica(clinica: clinica_schemas.ClinicaCreate, db: Session = Depends(get_db)):
    """
    Endpoint para cadastrar uma nova clínica. 
    """
    service = clinica_service.ClinicaService(db)
    return service.create_clinica(clinica)

@router.get("/", response_model=List[clinica_schemas.Clinica])
def list_clinicas(db: Session = Depends(get_db)):
    """
    Endpoint para listar todas as clínicas cadastradas.
    """
    service = clinica_service.ClinicaService(db)
    return service.get_all_clinicas()

@router.get("/{clinica_id}", response_model=clinica_schemas.Clinica)
def get_clinica(clinica_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para buscar uma clínica específica pelo seu ID. 
    """
    service = clinica_service.ClinicaService(db)
    db_clinica = service.get_clinica_by_id(clinica_id)
    if db_clinica is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clínica não encontrada")
    return db_clinica

@router.get("/{clinica_id}/veterinarios", response_model=List[veterinario_schemas.Veterinario])
def get_clinica_veterinarios(clinica_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os veterinários de uma clínica específica. 
    """
    service = clinica_service.ClinicaService(db)
    if not service.get_clinica_by_id(clinica_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clínica não encontrada")
    
    return service.get_veterinarios_by_clinica_id(clinica_id)
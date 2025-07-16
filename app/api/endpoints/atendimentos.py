from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import atendimento_service
from app.schemas import atendimento_schemas

router = APIRouter(
    prefix="/atendimentos",
    tags=["Atendimentos"]
)

@router.post("/", response_model=atendimento_schemas.Atendimento, status_code=status.HTTP_201_CREATED)
def create_atendimento(atendimento: atendimento_schemas.AtendimentoCreate, db: Session = Depends(get_db)):
    """
    Endpoint para registrar um novo atendimento.

    """
    service = atendimento_service.AtendimentoService(db)
   
    return service.create_atendimento(atendimento)

@router.get("/", response_model=List[atendimento_schemas.Atendimento])
def list_atendimentos(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os atendimentos registrados.
    """
    service = atendimento_service.AtendimentoService(db)
    return service.get_all_atendimentos()

@router.get("/{atendimento_id}", response_model=atendimento_schemas.Atendimento)
def get_atendimento(atendimento_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para buscar um atendimento específico pelo seu ID.
    """
    service = atendimento_service.AtendimentoService(db)
    db_atendimento = service.get_atendimento_by_id(atendimento_id)
    if db_atendimento is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Atendimento não encontrado")
    return db_atendimento
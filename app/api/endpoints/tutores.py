# app/api/endpoints/tutores.py

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import tutor_service
from app.schemas import tutor_schemas, pet_schemas

router = APIRouter(
    prefix="/tutores",
    tags=["Tutores"]
)

@router.post("/", response_model=tutor_schemas.Tutor, status_code=status.HTTP_201_CREATED)
def create_tutor(tutor: tutor_schemas.TutorCreate, db: Session = Depends(get_db)):
    """
    Endpoint para cadastrar um novo tutor.
    """
    service = tutor_service.TutorService(db)
    return service.create_tutor(tutor)

@router.get("/", response_model=List[tutor_schemas.Tutor])
def list_tutores(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os tutores cadastrados.
    """
    service = tutor_service.TutorService(db)
    return service.get_all_tutores()

@router.get("/{tutor_id}/pets", response_model=List[pet_schemas.Pet])
def get_tutor_pets(tutor_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os pets de um tutor específico.
    """
    service = tutor_service.TutorService(db)
    if not service.get_tutor_by_id(tutor_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tutor não encontrado"
        )
    return service.get_pets_by_tutor_id(tutor_id)
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import pet_service
from app.schemas import pet_schemas, atendimento_schemas

router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)

@router.post("/", response_model=pet_schemas.Pet, status_code=status.HTTP_201_CREATED)
def create_pet(pet: pet_schemas.PetCreate, db: Session = Depends(get_db)):
    """
    Endpoint para cadastrar um novo pet.
   .
    """
    service = pet_service.PetService(db)
    return service.create_pet(pet)

@router.get("/", response_model=List[pet_schemas.Pet])
def list_pets(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os pets cadastrados.
    """
    service = pet_service.PetService(db)
    return service.get_all_pets()

@router.get("/{pet_id}/atendimentos", response_model=List[atendimento_schemas.Atendimento])
def get_pet_atendimentos(pet_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os atendimentos de um pet específico.
    """
    service = pet_service.PetService(db)
    if not service.get_pet_by_id(pet_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet não encontrado"
        )
    return service.get_atendimentos_by_pet_id(pet_id)
from sqlalchemy.orm import Session
from typing import List, Optional 
from ..repositories.pet_repository import PetRepository
from ..repositories.tutor_repository import TutorRepository
from ..schemas import pet_schemas
from ..models import models
from fastapi import HTTPException, status

class PetService:
    def __init__(self, db: Session):
        self.repo = PetRepository(db)
        self.tutor_repo = TutorRepository(db)

    def create_pet(self, pet: pet_schemas.PetCreate) -> models.Pet:
        db_tutor = self.tutor_repo.get_tutor_by_id(pet.tutor_id)
        if not db_tutor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tutor com ID {pet.tutor_id} não encontrado."
            )

        db_pet = models.Pet(**pet.dict())
        return self.repo.create_pet(db_pet)

    def get_all_pets(self) -> List[models.Pet]:
        return self.repo.get_all_pets()
    
    def get_pet_by_id(self, pet_id: int) -> Optional[models.Pet]:
        return self.repo.get_pet_by_id(pet_id)

    def get_atendimentos_by_pet_id(self, pet_id: int) -> List[models.Atendimento]:
        return self.repo.get_atendimentos_by_pet_id(pet_id)
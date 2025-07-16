# veterinaria/services/atendimento_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.atendimento_repository import AtendimentoRepository
from app.repositories.pet_repository import PetRepository
from app.repositories.veterinario_repository import VeterinarioRepository
from app.schemas import atendimento_schemas
from app.models import models
class AtendimentoService:
    def __init__(self, db: Session):
        self.repo = AtendimentoRepository(db)
        self.pet_repo = PetRepository(db)
        self.vet_repo = VeterinarioRepository(db)

    def create_atendimento(self, atendimento: atendimento_schemas.AtendimentoCreate) -> models.Atendimento:
      
        # 1. Valida se o Pet existe
        if not self.pet_repo.get_pet_by_id(atendimento.pet_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pet com ID {atendimento.pet_id} não encontrado."
            )
        # 2. Valida se o Veterinário existe
        if not self.vet_repo.get_veterinario_by_id(atendimento.veterinario_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Veterinário com ID {atendimento.veterinario_id} não encontrado."
            )
        
        db_atendimento = models.Atendimento(**atendimento.dict())
        return self.repo.create_atendimento(db_atendimento)


    def get_all_atendimentos(self) -> list[models.Atendimento]:
        return self.repo.get_all_atendimentos()

    def get_atendimento_by_id(self, atendimento_id: int) -> models.Atendimento | None:
        return self.repo.get_atendimento_by_id(atendimento_id)
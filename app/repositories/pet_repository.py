from sqlalchemy.orm import Session
from ..models import models

class PetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_pet(self, pet: models.Pet) -> models.Pet:
        self.db.add(pet)
        self.db.commit()
        self.db.refresh(pet)
        return pet

    def get_all_pets(self) -> list[models.Pet]:
        return self.db.query(models.Pet).all()

    def get_pet_by_id(self, pet_id: int) -> models.Pet | None:
        return self.db.query(models.Pet).filter(models.Pet.id == pet_id).first()

    def get_atendimentos_by_pet_id(self, pet_id: int) -> list[models.Atendimento]:
        """
        Busca todos os atendimentos recebidos por um pet específico.
        Esta função suporta o endpoint GET /pets/{id}/atendimentos[cite: 78].
        """
        pet = self.get_pet_by_id(pet_id)
        if pet:
            return pet.atendimentos
        return []
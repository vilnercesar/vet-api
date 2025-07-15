from sqlalchemy.orm import Session
from ..models import models

class TutorRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_tutor(self, tutor: models.Tutor) -> models.Tutor:
        self.db.add(tutor)
        self.db.commit()
        self.db.refresh(tutor)
        return tutor

    def get_all_tutores(self) -> list[models.Tutor]:
        return self.db.query(models.Tutor).all()

    def get_tutor_by_id(self, tutor_id: int) -> models.Tutor | None:
        return self.db.query(models.Tutor).filter(models.Tutor.id == tutor_id).first()

    def get_pets_by_tutor_id(self, tutor_id: int) -> list[models.Pet]:
        """
        Busca todos os pets associados a um tutor específico.
        Esta função suporta o endpoint GET /tutores/{id}/pets.
        """
        tutor = self.get_tutor_by_id(tutor_id)
        if tutor:
            return tutor.pets
        return []
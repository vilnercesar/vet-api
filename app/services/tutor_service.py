
from sqlalchemy.orm import Session
from ..repositories.tutor_repository import TutorRepository
from ..schemas import tutor_schemas
from ..models import models

class TutorService:
    def __init__(self, db: Session):
        self.repo = TutorRepository(db)

    def create_tutor(self, tutor: tutor_schemas.TutorCreate) -> models.Tutor:
        db_tutor = models.Tutor(**tutor.dict())
        return self.repo.create_tutor(db_tutor)

    def get_all_tutores(self) -> list[models.Tutor]:
        return self.repo.get_all_tutores()

    def get_tutor_by_id(self, tutor_id: int) -> models.Tutor | None:
        return self.repo.get_tutor_by_id(tutor_id)

    def get_pets_by_tutor_id(self, tutor_id: int) -> list[models.Pet]:
        return self.repo.get_pets_by_tutor_id(tutor_id)
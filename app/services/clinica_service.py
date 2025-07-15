from sqlalchemy.orm import Session
from ..repositories.clinica_repository import ClinicaRepository
from ..schemas import clinica_schemas
from ..models import models

class ClinicaService:
    def __init__(self, db: Session):
        self.repo = ClinicaRepository(db)

    def create_clinica(self, clinica: clinica_schemas.ClinicaCreate) -> models.Clinica:
        """
        Lógica de negócio para criar uma clínica.
        Recebe um schema Pydantic, converte para um modelo SQLAlchemy e passa para o repositório.
        """
        db_clinica = models.Clinica(
            nome=clinica.nome,
            cidade=clinica.cidade
        )
        return self.repo.create_clinica(db_clinica)

    def get_all_clinicas(self) -> list[models.Clinica]:
        return self.repo.get_all_clinicas()

    def get_clinica_by_id(self, clinica_id: int) -> models.Clinica | None:
        return self.repo.get_clinica_by_id(clinica_id)
    
    def get_veterinarios_by_clinica_id(self, clinica_id: int) -> list[models.Veterinario]:
        return self.repo.get_veterinarios_by_clinica_id(clinica_id)
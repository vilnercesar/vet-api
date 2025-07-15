# veterinaria/services/veterinario_service.py
from sqlalchemy.orm import Session
from ..repositories.veterinario_repository import VeterinarioRepository
from ..repositories.clinica_repository import ClinicaRepository
from ..schemas import veterinario_schemas
from ..models import models
from fastapi import HTTPException, status

class VeterinarioService:
    def __init__(self, db: Session):
        self.repo = VeterinarioRepository(db)
        self.clinica_repo = ClinicaRepository(db)

    def create_veterinario(self, veterinario: veterinario_schemas.VeterinarioCreate) -> models.Veterinario:
        """
        Lógica de negócio para criar um veterinário.
        """

        db_clinica = self.clinica_repo.get_clinica_by_id(veterinario.clinica_id)
        if not db_clinica:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Clínica com ID {veterinario.clinica_id} não encontrada."
            )

        db_veterinario = models.Veterinario(
            nome=veterinario.nome,
            especialidade=veterinario.especialidade,
            clinica_id=veterinario.clinica_id
        )
        return self.repo.create_veterinario(db_veterinario)

    def get_all_veterinarios(self) -> list[models.Veterinario]:
        return self.repo.get_all_veterinarios()

    def get_veterinario_by_id(self, veterinario_id: int) -> models.Veterinario | None:
        return self.repo.get_veterinario_by_id(veterinario_id)
    
    def get_atendimentos_by_veterinario_id(self, veterinario_id: int) -> list[models.Atendimento]:
        return self.repo.get_atendimentos_by_veterinario_id(veterinario_id)
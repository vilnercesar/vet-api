from sqlalchemy.orm import Session
from ..models import models

class VeterinarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_veterinario(self, veterinario: models.Veterinario) -> models.Veterinario:
        self.db.add(veterinario)
        self.db.commit()
        self.db.refresh(veterinario)
        return veterinario

    def get_all_veterinarios(self) -> list[models.Veterinario]:
        return self.db.query(models.Veterinario).all()

    def get_veterinario_by_id(self, veterinario_id: int) -> models.Veterinario | None:
        return self.db.query(models.Veterinario).filter(models.Veterinario.id == veterinario_id).first()
    
    def get_atendimentos_by_veterinario_id(self, veterinario_id: int) -> list[models.Atendimento]:
        """
        Busca todos os atendimentos realizados por um veterinário específico.
        Esta função suporta o endpoint GET /veterinarios/{id}/atendimentos.
        """
        veterinario = self.get_veterinario_by_id(veterinario_id)
        if veterinario:
            return veterinario.atendimentos
        return []
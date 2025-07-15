from sqlalchemy.orm import Session
from ..models import models

class AtendimentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_atendimento(self, atendimento: models.Atendimento) -> models.Atendimento:
        self.db.add(atendimento)
        self.db.commit()
        self.db.refresh(atendimento)
        return atendimento

    def get_all_atendimentos(self) -> list[models.Atendimento]:
        return self.db.query(models.Atendimento).all()

    def get_atendimento_by_id(self, atendimento_id: int) -> models.Atendimento | None:
        return self.db.query(models.Atendimento).filter(models.Atendimento.id == atendimento_id).first()
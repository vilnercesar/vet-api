from sqlalchemy.orm import Session
from ..models import models

class ClinicaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_clinica(self, clinica: models.Clinica) -> models.Clinica:
        """
        Adiciona uma nova clínica ao banco de dados.
        :param clinica: O objeto Clinica a ser adicionado.
        :return: O objeto Clinica que foi adicionado com o id preenchido.
        """
        self.db.add(clinica)
        self.db.commit()
        self.db.refresh(clinica)
        return clinica

    def get_all_clinicas(self) -> list[models.Clinica]:
        """
        Retorna uma lista de todas as clínicas cadastradas.
        :return: Uma lista de objetos Clinica.
        """
        return self.db.query(models.Clinica).all()

    def get_clinica_by_id(self, clinica_id: int) -> models.Clinica | None:
        """
        Busca uma clínica específica pelo seu ID.
        :param clinica_id: O ID da clínica a ser buscada.
        :return: O objeto Clinica correspondente ou None se não for encontrada.
        """
        return self.db.query(models.Clinica).filter(models.Clinica.id == clinica_id).first()

    def get_veterinarios_by_clinica_id(self, clinica_id: int) -> list[models.Veterinario]:
        """
        Busca todos os veterinários associados a uma clínica específica.
        :param clinica_id: O ID da clínica.
        :return: Uma lista de objetos Veterinario.
        """
        clinica = self.get_clinica_by_id(clinica_id)
        if clinica:
            return clinica.veterinarios
        return []
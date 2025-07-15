from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from ..database import Base

class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cidade = Column(String)
    
    veterinarios = relationship("Veterinario", back_populates="clinica")

class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    especialidade = Column(String)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"))
   
    clinica = relationship("Clinica", back_populates="veterinarios")
    atendimentos = relationship("Atendimento", back_populates="veterinario")

class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    telefone = Column(String)

    pets = relationship("Pet", back_populates="tutor")

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    especie = Column(String)
    idade = Column(Integer)
    tutor_id = Column(Integer, ForeignKey("tutores.id"))
    tutor = relationship("Tutor", back_populates="pets")
    atendimentos = relationship("Atendimento", back_populates="pet")

class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, default=datetime.utcnow)
    descricao = Column(String)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"))

    pet = relationship("Pet", back_populates="atendimentos")
    veterinario = relationship("Veterinario", back_populates="atendimentos")
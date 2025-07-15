# veterinaria/main.py

from fastapi import FastAPI
from .models import models
from .database import engine
from .api.endpoints import clinicas # Importa o módulo de endpoints de clinicas

# Cria as tabelas no banco de dados (se não existirem)
models.Base.metadata.create_all(bind=engine)

# Cria a instância principal da aplicação FastAPI
app = FastAPI(
    title="API de Gerenciamento de Clínicas Veterinárias",
    description="Sistema para gerenciar clínicas, veterinários, tutores, pets e atendimentos.",
    version="1.0.0"
)


app.include_router(clinicas.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Clínicas Veterinárias!"}
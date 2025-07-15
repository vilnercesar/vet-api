import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("Variável de ambiente DATABASE_URL não foi definida.")

# Cria a engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Cria uma classe de sessão configurada

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe Base para os modelos declarativos do ORM

Base = declarative_base()



def get_db():
    """
    Função geradora para fornecer uma sessão de banco de dados por requisição.
    Garante que a sessão seja sempre fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
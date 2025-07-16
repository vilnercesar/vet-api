# Sistema de Gestão de Clínicas Veterinárias (Vet-API)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-05998b?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-c4263d?logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?logo=postgresql&logoColor=white)

API RESTful desenvolvida para gerir uma rede de clínicas veterinárias, permitindo o cadastro e a gestão de clínicas, veterinários, tutores, pets e seus respectivos atendimentos.


## Tecnologias Utilizadas

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
* **Banco de Dados:** [PostgreSQL](https://www.postgresql.org/)
* **ORM (Object-Relational Mapper):** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Validação de Dados:** [Pydantic](https://docs.pydantic.dev/)
* **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
* **Gestão de Variáveis de Ambiente:** [python-dotenv](https://pypi.org/project/python-dotenv/)

## Estrutura do Projeto

O projeto segue uma arquitetura em camadas para separar as responsabilidades:

```
VET-API/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── endpoints/
│   │       ├── clinicas.py
│   │       ├── veterinarios.py
│   │       ├── tutores.py
│   │       ├── pets.py
│   │       └── atendimentos.py
│   ├── models/
│   │   └── models.py
│   ├── repositories/
│   │   ├── clinica_repository.py
│   │   └── ...
│   ├── schemas/
│   │   ├── clinica_schemas.py
│   │   └── ...
│   ├── services/
│   │   ├── clinica_service.py
│   │   └── ...
│   ├── database.py
│   └── main.py
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

## Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Pré-requisitos

* [Python](https://www.python.org/downloads/) (versão 3.9 ou superior)
* [PostgreSQL](https://www.postgresql.org/download/) instalado e a correr.

### 2. Clonar o Repositório

```bash
git clone https://github.com/vilnercesar/vet-api.git
cd vet-api
```

### 3. Criar e Ativar o Ambiente Virtual

É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.

* **No Windows:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```

* **No Linux ou macOS:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

### 4. Instalar as Dependências

Com o ambiente virtual ativo, instale todas as bibliotecas necessárias.

```bash
pip install -r requirements.txt
```

### 5. Configurar o Banco de Dados

1.  **Crie um banco de dados** no PostgreSQL para este projeto. Sugestão de nome: `vet_db`.
2.  **Copie o arquivo de exemplo** `.env.example` para um novo arquivo chamado `.env`.

    * **No Windows:**
        ```powershell
        copy .env.example .env
        ```
    * **No Linux ou macOS:**
        ```bash
        cp .env.example .env
        ```
3.  **Edite o arquivo `.env`** com as suas credenciais reais do PostgreSQL.

    ```ini
    # Exemplo de conteúdo para o arquivo .env
    DATABASE_URL="postgresql://seu_usuario:sua_senha@localhost:5432/vet_db"
    ```

## Executar a Aplicação

Com o ambiente configurado, inicie o servidor FastAPI com o Uvicorn.

```bash
uvicorn app.main:app --reload
```

O servidor estará rodando e acessível em `http://127.0.0.1:8000`. A opção `--reload` faz com que o servidor reinicie automaticamente após qualquer alteração no código.

## Utilizar a API

Após iniciar a aplicação, a documentação interativa (Swagger UI) estará disponível automaticamente. Acesse ao seguinte URL no seu navegador para ver e testar todos os endpoints:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## Endpoints da API

A seguir, uma lista dos principais endpoints disponíveis:

### Clínicas
* `POST /clinicas`: Cadastra uma nova clínica.
* `GET /clinicas`: Lista todas as clínicas.
* `GET /clinicas/{id}`: Obtém os detalhes de uma clínica específica.
* `GET /clinicas/{id}/veterinarios`: Lista os veterinários de uma clínica.

### Veterinários
* `POST /veterinarios`: Cadastra um novo veterinário.
* `GET /veterinarios`: Lista todos os veterinários.
* `GET /veterinarios/{id}/atendimentos`: Lista os atendimentos de um veterinário.

### Tutores
* `POST /tutores`: Cadastra um novo tutor.
* `GET /tutores`: Lista todos os tutores.
* `GET /tutores/{id}/pets`: Lista os pets de um tutor.

### Pets
* `POST /pets`: Cadastra um novo pet.
* `GET /pets`: Lista todos os pets.
* `GET /pets/{id}/atendimentos`: Lista os atendimentos de um pet.

### Atendimentos
* `POST /atendimentos`: Regista um novo atendimento.
* `GET /atendimentos`: Lista todos os atendimentos.
* `GET /atendimentos/{id}`: Obtém os detalhes de um atendimento específico.

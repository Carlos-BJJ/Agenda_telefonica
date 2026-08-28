# Agenda Telefônica

Sistema de agenda telefônica em Python com operações de **CRUD** (Create, Read, Update, Delete) de contatos — nome, telefone e email.

O projeto começou com persistência em `contatos.json` e evoluiu para usar um banco **PostgreSQL**.

## Funcionalidades

- Adicionar contato
- Buscar contato (por nome, busca parcial)
- Listar todos os contatos
- Editar contato existente
- Remover contato

## Estrutura do projeto

```
Agenda_telefonica/
├── agenda_final.py       # Menu principal (terminal), usa match/case e while
├── menu_agenda.py         # Módulo com as funções de CRUD e acesso ao banco
└── contatos.json           # (legado) persistência original em JSON
```

## Persistência de dados

O projeto migrou de um arquivo `contatos.json` para um banco **PostgreSQL**, usando o `nome` do contato como chave primária:

```sql
CREATE TABLE contatos (
    nome     VARCHAR(100) PRIMARY KEY,
    telefone VARCHAR(20) NOT NULL,
    email    VARCHAR(100) NOT NULL
);
```
## Instalação

```bash
git clone https://github.com/Carlos-BJJ/Agenda_telefonica.git
cd Agenda_telefonica
pip install psycopg2-binary
```

Crie o banco no PostgreSQL:

```sql
CREATE DATABASE agenda_db;
```

## Tecnologias usadas

- Python 3
- PostgreSQL + psycopg2

## Próximos passos

- [ ] Validação de formato de telefone/email
- [ ] Testes automatizados
- [ ] Autenticação de usuário (se o projeto crescer para multiusuário)

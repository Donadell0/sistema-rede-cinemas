# 🎬 Sistema de Rede de Cinemas

Atividade acadêmica desenvolvida para a disciplina de **Engenharia de Software**.  
Demonstra a aplicação de UML, arquitetura MVC em camadas e persistência com SQLite.

## Tecnologias

- Python 3.11+
- Flask 3.0
- SQLite (via módulo nativo `sqlite3`)
- Arquitetura MVC com camadas Service e Repository

## Estrutura do Projeto

```
sistema-rede-cinemas/
├── docs/                    # Documentação UML e requisitos
│   ├── requisitos.md
│   ├── casos-de-uso.md
│   ├── diagrama-classes.md
│   ├── diagramas-atividade.md
│   └── diagramas-sequencia.md
├── app/
│   ├── models/database.py   # Schema e conexão SQLite
│   ├── repositories/        # Acesso ao banco de dados
│   ├── services/            # Regras de negócio
│   └── controllers/         # Rotas HTTP (Flask Blueprints)
├── run.py                   # Ponto de entrada
└── requirements.txt
```

## Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/sistema-rede-cinemas.git
cd sistema-rede-cinemas

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python run.py
```

O banco de dados SQLite é criado automaticamente em `instance/cinema.db` com dados de exemplo.

## Endpoints Disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/filmes` | Lista todos os filmes |
| GET | `/filmes/{id}` | Detalhes e elenco do filme |
| POST | `/filmes` | Cadastrar novo filme |
| GET | `/cinemas` | Lista cinemas |
| GET | `/cinemas/{id}/sessoes` | Sessões de um cinema |
| GET | `/cinemas/{id}/publico` | Total de público do cinema |
| POST | `/sessoes` | Cadastrar sessão (valida conflito) |
| GET | `/sessoes/{id}/publico` | Total de público da sessão |
| POST | `/publico` | Registrar público diário |
| GET | `/publico/filme/{id}` | Total de público do filme |

## Exemplo de Uso

```bash
# Listar filmes
curl http://localhost:5000/filmes

# Cadastrar sessão
curl -X POST http://localhost:5000/sessoes \
  -H "Content-Type: application/json" \
  -d '{"cinema_id":1,"filme_id":2,"data_hora":"2025-10-05 19:00","sala":"Sala 1"}'

# Total de público de um cinema
curl http://localhost:5000/cinemas/1/publico
```

## Arquitetura

```
Request HTTP
    ↓
Controller  → recebe e valida a requisição, retorna JSON
    ↓
Service     → aplica regras de negócio e validações
    ↓
Repository  → executa SQL, abstrai o banco de dados
    ↓
SQLite      → persistência dos dados
```

## Documentação

| Documento | Descrição |
|-----------|-----------|
| [Requisitos](docs/requisitos.md) | Requisitos funcionais e regras de negócio |
| [Casos de Uso](docs/casos-de-uso.md) | Diagrama e descrição dos casos de uso |
| [Diagrama de Classes](docs/diagrama-classes.md) | Modelo do domínio |
| [Diagramas de Atividade](docs/diagramas-atividade.md) | Fluxos de processo |
| [Diagramas de Sequência](docs/diagramas-sequencia.md) | Interação entre camadas |

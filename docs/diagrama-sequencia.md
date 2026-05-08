# Diagramas de Sequência

Os diagramas mostram a interação entre as camadas da arquitetura MVC:
**Controller → Service → Repository → SQLite**.

---

## DS01 – Cadastrar Sessão

Fluxo completo desde a requisição HTTP até a persistência, incluindo os caminhos de erro.

```plantuml
@startuml
actor Cliente
participant "Controller\n(controllers.py)" as C
participant "Service\n(services.py)" as S
participant "Repository\n(repositories.py)" as R
database "SQLite\n(cinema.db)" as DB

Cliente -> C : POST /sessoes\n{cinema_id, filme_id,\n data_hora, sala}
activate C

C -> S : cadastrar_sessao(dados)
activate S

S -> R : cinema_repo.find_by_id(cinema_id)
activate R
R -> DB : SELECT * FROM cinema WHERE id=?
DB --> R : row | None
R --> S : cinema | None
deactivate R

alt Cinema não encontrado
  S --> C : raise ValueError
  C --> Cliente : 400 {"erro": "Cinema não encontrado"}
end

S -> R : filme_repo.find_by_id(filme_id)
activate R
R -> DB : SELECT * FROM filme WHERE id=?
DB --> R : row
R --> S : filme
deactivate R

S -> R : sessao_repo.check_conflict(\n  cinema_id, sala, data_hora, duracao)
activate R
R -> DB : SELECT s.data_hora, f.duracao_min\nFROM sessao s JOIN filme f ...
DB --> R : sessões existentes
R --> S : True | False
deactivate R

alt Conflito de horário
  S --> C : raise ValueError
  C --> Cliente : 400 {"erro": "Conflito de horário"}
end

S -> R : sessao_repo.save(\n  cinema_id, filme_id, data_hora, sala)
activate R
R -> DB : INSERT INTO sessao (...)
DB --> R : lastrowid
R --> S : novo_id
deactivate R

S --> C : {"id": novo_id, "mensagem": "..."}
deactivate S

C --> Cliente : 201 {"id": 5, "mensagem": "Sessão cadastrada"}
deactivate C
@enduml
```

---

<img width="1258" height="1024" alt="1111111" src="https://github.com/user-attachments/assets/928d7535-b3f5-4241-b32a-a97a20ef40a6" />

## DS02 – Consultar Público por Cinema

Fluxo de leitura mostrando como a agregação SQL percorre as camadas até retornar ao cliente.

```plantuml
@startuml
actor Cliente
participant "Controller\n(controllers.py)" as C
participant "Service\n(services.py)" as S
participant "Repository\n(repositories.py)" as R
database "SQLite\n(cinema.db)" as DB

Cliente -> C : GET /cinemas/{id}/publico
activate C

C -> S : total_por_cinema(cinema_id)
activate S

S -> R : cinema_repo.find_by_id(cinema_id)
activate R
R -> DB : SELECT * FROM cinema WHERE id=?
DB --> R : row
R --> S : cinema
deactivate R

S -> R : publico_repo.total_por_cinema(cinema_id)
activate R
R -> DB : SELECT SUM(rp.publico)\nFROM registro_publico rp\nJOIN sessao s ON s.id = rp.sessao_id\nWHERE s.cinema_id = ?
DB --> R : total
R --> S : Integer
deactivate R

S --> C : {"cinema": "CineMax Centro",\n "total_publico": 410}
deactivate S

C --> Cliente : 200 {"cinema": "...", "total_publico": 410}
deactivate C
@enduml
```
<img width="1194" height="597" alt="zzzzzzzzzzz" src="https://github.com/user-attachments/assets/6c7c5e07-bc04-4a95-ad09-27b18fc40d2e" />

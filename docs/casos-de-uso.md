# Diagrama de Casos de Uso

## Atores

- **Funcionário/Administrador** — responsável pela gestão do sistema
- **Espectador** — acesso somente leitura a filmes e sessões

## Diagrama

> Renderize em [PlantUML Online](https://www.plantuml.com/plantuml/uml/) ou instale a extensão PlantUML no VS Code.

```plantuml
@startuml
left to right direction
skinparam actorStyle awesome

actor "Funcionário/\nAdministrador" as F
actor "Espectador" as E

rectangle "Sistema de Cinema" {
  usecase "Cadastrar Filme"    as UC1
  usecase "Cadastrar Cinema"   as UC2
  usecase "Gerenciar Sessão"   as UC3
  usecase "Registrar Público"  as UC4
  usecase "Consultar Público"  as UC5
  usecase "Consultar Filmes"   as UC6
  usecase "Consultar Sessões"  as UC7
  usecase "Ver Elenco/Diretor" as UC8
}

F --> UC1
F --> UC2
F --> UC3
F --> UC4
F --> UC5

E --> UC6
E --> UC7
E --> UC8

UC5 ..> UC6 : «include»
@enduml
```
<img width="612" height="547" alt="2222222222222" src="https://github.com/user-attachments/assets/2316a2b8-9a8b-464f-ae5e-935b0f2de464" />


## Descrição dos Casos de Uso

| ID  | Nome | Ator | Descrição |
|-----|------|------|-----------|
| UC1 | Cadastrar Filme | Funcionário | Registra novo filme com todos os dados |
| UC2 | Cadastrar Cinema | Funcionário | Registra unidade da rede com endereço e capacidade |
| UC3 | Gerenciar Sessão | Funcionário | Cria sessão validando conflito de horário |
| UC4 | Registrar Público | Funcionário | Lança público diário de uma sessão |
| UC5 | Consultar Público | Funcionário | Totaliza público por sessão, filme ou cinema |
| UC6 | Consultar Filmes | Espectador | Lista filmes em cartaz |
| UC7 | Consultar Sessões | Espectador | Lista sessões por cinema |
| UC8 | Ver Elenco/Diretor | Espectador | Exibe detalhes do filme |

# Diagrama de Classes do Domínio

> Renderize em [PlantUML Online](https://www.plantuml.com/plantuml/uml/).

```plantuml
@startuml
hide methods
skinparam classBackgroundColor #E6F1FB
skinparam classBorderColor #378ADD

class Cinema {
  id : Integer
  nome : String
  cidade : String
  estado : String
  endereco : String
  capacidade : Integer
}

class Filme {
  id : Integer
  titulo : String
  genero : String
  duracao_min : Integer
  diretor : String
  elenco : String
}

class Sessao {
  id : Integer
  cinema_id : Integer
  filme_id : Integer
  data_hora : DateTime
  sala : String
}

class RegistroPublico {
  id : Integer
  sessao_id : Integer
  data : Date
  publico : Integer
}

Cinema "1" --> "0..*" Sessao
Filme   "1" --> "0..*" Sessao
Sessao  "1" --> "0..*" RegistroPublico
@enduml
```

## Descrição das Entidades

| Entidade | Responsabilidade |
|----------|-----------------|
| `Cinema` | Representa uma unidade física da rede |
| `Filme` | Representa um filme com seus metadados |
| `Sessao` | Elo entre cinema e filme em data/hora/sala específicos |
| `RegistroPublico` | Registro diário de espectadores por sessão |

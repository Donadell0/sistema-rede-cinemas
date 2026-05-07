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
<img width="378" height="505" alt="TP71IWCn48RlUOgmteGMYw3YGMfR2zx4UYzZCcw79faoIKxYknkxssBMzRJCDvdytqxcCO6ax9tQaKNjCUtOHXNt50uWuBLn4EC2pBuLpi4ksR7eYwURzMoz-7ECnQBqHwvlxnvNAwME7RsaW1xqfzAQhBxNpo5XYrBAm1uBs2IXq9RQa0LR4IoEbYiIIWwQYXaum6dsVFtNANzDpkDOVA" src="https://github.com/user-attachments/assets/4ab0c2c3-4a1f-4d53-abab-2be961ebd8f0" />


## Descrição das Entidades

| Entidade | Responsabilidade |
|----------|-----------------|
| `Cinema` | Representa uma unidade física da rede |
| `Filme` | Representa um filme com seus metadados |
| `Sessao` | Elo entre cinema e filme em data/hora/sala específicos |
| `RegistroPublico` | Registro diário de espectadores por sessão |

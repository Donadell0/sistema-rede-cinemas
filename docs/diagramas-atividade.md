# Diagramas de Atividade

## DA01 – Cadastrar Sessão

Fluxo de negócio para adicionar uma sessão, incluindo validação de conflito de horário.

```plantuml
@startuml
|Funcionário|
start
:Informar cinema, filme,\ndata/hora e sala;

|Sistema|
:Verificar se cinema existe;
if (Cinema válido?) then (não)
  :Retornar erro "Cinema não encontrado";
  stop
endif

:Verificar se filme existe;
if (Filme válido?) then (não)
  :Retornar erro "Filme não encontrado";
  stop
endif

:Verificar conflito de horário\n(sessões existentes na mesma sala);
note right: Intervalo mínimo: 30 min\napós término da sessão anterior

if (Há conflito?) then (sim)
  :Retornar erro "Conflito de horário";
  stop
endif

:Persistir sessão no banco;
:Retornar confirmação;

|Funcionário|
:Exibir mensagem de sucesso;
stop
@enduml
```
<img width="763" height="1056" alt="1111" src="https://github.com/user-attachments/assets/4dfdcda8-85fa-4401-8f48-3c310d69e2b9" />


---

## DA02 – Registrar Público

Fluxo para lançar o público diário de uma sessão com validações de entrada.

```plantuml
@startuml
|Funcionário|
start
:Informar sessão, data e\nquantidade de espectadores;

|Sistema|
:Validar campos obrigatórios;
if (Dados válidos?) then (não)
  :Retornar erro de validação;
  stop
endif

:Verificar se público >= 0;
if (Público negativo?) then (sim)
  :Retornar erro "Público inválido";
  stop
endif

:Persistir registro de público;
:Retornar confirmação;

|Funcionário|
:Exibir confirmação;
stop
@enduml
```
<img width="494" height="813" alt="22222" src="https://github.com/user-attachments/assets/a302e732-a7f6-477a-bf81-962662456ffa" />

---

## DA03 – Consultar Totais de Público

Fluxo de consulta agregada de público, podendo ser por sessão, filme ou cinema.

```plantuml
@startuml
|Usuário|
start
:Selecionar tipo de consulta\n(sessão / filme / cinema);

|Sistema|
if (Por sessão?) then (sim)
  :Somar público de todos os\nregistros da sessão;
else if (Por filme?) then (sim)
  :Somar público de todas as\nsessões do filme;
else
  :Somar público de todas as\nsessões do cinema;
endif

:Retornar total ao usuário;

|Usuário|
```
<img width="809" height="446" alt="333333" src="https://github.com/user-attachments/assets/8744b7af-817a-49d1-9853-e7769fe2cbb0" />

:Visualizar resultado;
stop
@enduml
```

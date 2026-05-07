# Requisitos do Sistema

## Requisitos Funcionais

| Código | Descrição |
|--------|-----------|
| RF01 | Cadastrar filmes com título, gênero, duração, diretor e elenco |
| RF02 | Cadastrar cinemas com nome, endereço, cidade, estado e capacidade |
| RF03 | Gerenciar sessões associando filme a cinema com data/hora e sala |
| RF04 | Registrar público diário por sessão |
| RF05 | Consultar totais de público por sessão, por filme e por cinema |
| RF06 | Consultar elenco, diretor e gênero de cada filme |

## Regras de Negócio

| Código | Regra |
|--------|-------|
| RN01 | Entre o término de uma sessão e o início da próxima na mesma sala deve haver intervalo mínimo de 30 minutos |
| RN02 | O público registrado por sessão não pode ser negativo |
| RN03 | Não é permitido cadastrar sessão sem filme ou cinema válido |
| RN04 | A duração do filme deve ser maior que zero |
| RN05 | A capacidade do cinema é informativa; controle de lotação fora do escopo desta versão |

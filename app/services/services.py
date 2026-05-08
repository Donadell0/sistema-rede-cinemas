from app.repositories.repositories import (
    FilmeRepository, SessaoRepository, PublicoRepository, CinemaRepository
)

filme_repo = FilmeRepository()
sessao_repo = SessaoRepository()
publico_repo = PublicoRepository()
cinema_repo = CinemaRepository()


class FilmeService:
    def listar_filmes(self):
        return filme_repo.find_all()

    def buscar_filme(self, filme_id):
        filme = filme_repo.find_by_id(filme_id)
        if not filme:
            raise ValueError(f"Filme com id {filme_id} não encontrado.")
        return filme

    def cadastrar_filme(self, dados):
        campos = ['titulo', 'genero', 'duracao_min', 'diretor', 'elenco']
        for c in campos:
            if not dados.get(c):
                raise ValueError(f"Campo obrigatório ausente: {c}")
        if int(dados['duracao_min']) <= 0:
            raise ValueError("Duração deve ser maior que zero.")
        novo_id = filme_repo.save(
            dados['titulo'], dados['genero'],
            int(dados['duracao_min']), dados['diretor'], dados['elenco']
        )
        return filme_repo.find_by_id(novo_id)


class SessaoService:
    def listar_por_cinema(self, cinema_id):
        cinema = cinema_repo.find_by_id(cinema_id)
        if not cinema:
            raise ValueError("Cinema não encontrado.")
        return sessao_repo.find_by_cinema(cinema_id)

    def cadastrar_sessao(self, dados):
        cinema = cinema_repo.find_by_id(dados.get('cinema_id'))
        if not cinema:
            raise ValueError("Cinema não encontrado.")
        filme = filme_repo.find_by_id(dados.get('filme_id'))
        if not filme:
            raise ValueError("Filme não encontrado.")
        if not dados.get('data_hora') or not dados.get('sala'):
            raise ValueError("Data/hora e sala são obrigatórios.")

        conflito = sessao_repo.check_conflict(
            dados['cinema_id'], dados['sala'],
            dados['data_hora'], filme['duracao_min']
        )
        if conflito:
            raise ValueError("Conflito de horário: outra sessão já ocupa esta sala neste intervalo (incluindo intervalo mínimo de 30 min).")

        novo_id = sessao_repo.save(
            dados['cinema_id'], dados['filme_id'],
            dados['data_hora'], dados['sala']
        )
        return {"id": novo_id, "mensagem": "Sessão cadastrada com sucesso."}


class PublicoService:
    def registrar_publico(self, dados):
        if not dados.get('sessao_id') or not dados.get('data') or dados.get('publico') is None:
            raise ValueError("sessao_id, data e publico são obrigatórios.")
        publico = int(dados['publico'])
        if publico < 0:
            raise ValueError("Público não pode ser negativo.")
        publico_repo.save(dados['sessao_id'], dados['data'], publico)
        return {"mensagem": "Público registrado com sucesso."}

    def total_por_sessao(self, sessao_id):
        return {"sessao_id": sessao_id, "total_publico": publico_repo.total_por_sessao(sessao_id)}

    def total_por_cinema(self, cinema_id):
        cinema = cinema_repo.find_by_id(cinema_id)
        nome = cinema['nome'] if cinema else str(cinema_id)
        return {"cinema": nome, "total_publico": publico_repo.total_por_cinema(cinema_id)}

    def total_por_filme(self, filme_id):
        filme = filme_repo.find_by_id(filme_id)
        titulo = filme['titulo'] if filme else str(filme_id)
        return {"filme": titulo, "total_publico": publico_repo.total_por_filme(filme_id)}


class CinemaService:
    def listar_cinemas(self):
        return cinema_repo.find_all()

    def buscar_cinema(self, cinema_id):
        cinema = cinema_repo.find_by_id(cinema_id)
        if not cinema:
            raise ValueError("Cinema não encontrado.")
        return cinema


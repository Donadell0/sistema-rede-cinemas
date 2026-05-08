from flask import Blueprint, request, jsonify
from app.services.services import FilmeService, SessaoService, PublicoService, CinemaService

filmes_bp = Blueprint('filmes', __name__, url_prefix='/filmes')
sessoes_bp = Blueprint('sessoes', __name__, url_prefix='/sessoes')
publico_bp = Blueprint('publico', __name__, url_prefix='/publico')
cinemas_bp = Blueprint('cinemas', __name__, url_prefix='/cinemas')

filme_service = FilmeService()
sessao_service = SessaoService()
publico_service = PublicoService()
cinema_service = CinemaService()


# ──────────────────────────────────────────────
# FILMES
# ──────────────────────────────────────────────
@filmes_bp.route('', methods=['GET'])
def listar_filmes():
    return jsonify(filme_service.listar_filmes()), 200

@filmes_bp.route('/<int:filme_id>', methods=['GET'])
def buscar_filme(filme_id):
    try:
        return jsonify(filme_service.buscar_filme(filme_id)), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

@filmes_bp.route('', methods=['POST'])
def cadastrar_filme():
    try:
        dados = request.get_json(force=True)
        filme = filme_service.cadastrar_filme(dados)
        return jsonify(filme), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


# ──────────────────────────────────────────────
# CINEMAS
# ──────────────────────────────────────────────
@cinemas_bp.route('', methods=['GET'])
def listar_cinemas():
    return jsonify(cinema_service.listar_cinemas()), 200

@cinemas_bp.route('/<int:cinema_id>', methods=['GET'])
def buscar_cinema(cinema_id):
    try:
        return jsonify(cinema_service.buscar_cinema(cinema_id)), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

@cinemas_bp.route('/<int:cinema_id>/sessoes', methods=['GET'])
def sessoes_do_cinema(cinema_id):
    try:
        return jsonify(sessao_service.listar_por_cinema(cinema_id)), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

@cinemas_bp.route('/<int:cinema_id>/publico', methods=['GET'])
def publico_cinema(cinema_id):
    return jsonify(publico_service.total_por_cinema(cinema_id)), 200


# ──────────────────────────────────────────────
# SESSÕES
# ──────────────────────────────────────────────
@sessoes_bp.route('', methods=['POST'])
def cadastrar_sessao():
    try:
        dados = request.get_json(force=True)
        resultado = sessao_service.cadastrar_sessao(dados)
        return jsonify(resultado), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@sessoes_bp.route('/<int:sessao_id>/publico', methods=['GET'])
def publico_sessao(sessao_id):
    return jsonify(publico_service.total_por_sessao(sessao_id)), 200


# ──────────────────────────────────────────────
# PÚBLICO
# ──────────────────────────────────────────────
@publico_bp.route('', methods=['POST'])
def registrar_publico():
    try:
        dados = request.get_json(force=True)
        resultado = publico_service.registrar_publico(dados)
        return jsonify(resultado), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@publico_bp.route('/filme/<int:filme_id>', methods=['GET'])
def publico_filme(filme_id):
    return jsonify(publico_service.total_por_filme(filme_id)), 200


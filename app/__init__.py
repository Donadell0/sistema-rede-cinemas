from flask import Flask
from app.models.database import init_db
from app.controllers.controllers import filmes_bp, sessoes_bp, publico_bp, cinemas_bp

def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(filmes_bp)
    app.register_blueprint(sessoes_bp)
    app.register_blueprint(publico_bp)
    app.register_blueprint(cinemas_bp)
    return app


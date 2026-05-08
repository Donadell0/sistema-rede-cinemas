import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../../instance/cinema.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS cinema (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            endereco TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS filme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            duracao_min INTEGER NOT NULL,
            diretor TEXT NOT NULL,
            elenco TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sessao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id INTEGER NOT NULL,
            filme_id INTEGER NOT NULL,
            data_hora TEXT NOT NULL,
            sala TEXT NOT NULL,
            FOREIGN KEY (cinema_id) REFERENCES cinema(id),
            FOREIGN KEY (filme_id) REFERENCES filme(id)
        );

        CREATE TABLE IF NOT EXISTS registro_publico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sessao_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            publico INTEGER NOT NULL,
            FOREIGN KEY (sessao_id) REFERENCES sessao(id)
        );
    """)

    # Seed data
    cursor.execute("SELECT COUNT(*) FROM cinema")
    if cursor.fetchone()[0] == 0:
        cursor.executescript("""
            INSERT INTO cinema (nome, cidade, estado, endereco, capacidade) VALUES
                ('CineMax Centro', 'São Paulo', 'SP', 'Av. Paulista, 1000', 300),
                ('CineMax Norte', 'São Paulo', 'SP', 'Av. Santana, 500', 250),
                ('CineMax Curitiba', 'Curitiba', 'PR', 'Rua das Flores, 200', 200);

            INSERT INTO filme (titulo, genero, duracao_min, diretor, elenco) VALUES
                ('Interestelar', 'Ficção Científica', 169, 'Christopher Nolan', 'Matthew McConaughey, Anne Hathaway'),
                ('Oppenheimer', 'Drama Histórico', 180, 'Christopher Nolan', 'Cillian Murphy, Emily Blunt'),
                ('Duna: Parte 2', 'Ficção Científica', 167, 'Denis Villeneuve', 'Timothée Chalamet, Zendaya');

            INSERT INTO sessao (cinema_id, filme_id, data_hora, sala) VALUES
                (1, 1, '2025-10-01 14:00', 'Sala 1'),
                (1, 2, '2025-10-01 18:00', 'Sala 2'),
                (2, 3, '2025-10-01 15:30', 'Sala 1'),
                (3, 1, '2025-10-01 16:00', 'Sala 1');

            INSERT INTO registro_publico (sessao_id, data, publico) VALUES
                (1, '2025-10-01', 220),
                (2, '2025-10-01', 190),
                (3, '2025-10-01', 175),
                (4, '2025-10-01', 160);
        """)

    conn.commit()
    conn.close()


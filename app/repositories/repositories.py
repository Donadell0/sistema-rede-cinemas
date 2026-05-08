from app.models.database import get_connection

class FilmeRepository:
    def find_all(self):
        conn = get_connection()
        rows = conn.execute("SELECT * FROM filme ORDER BY titulo").fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def find_by_id(self, filme_id):
        conn = get_connection()
        row = conn.execute("SELECT * FROM filme WHERE id = ?", (filme_id,)).fetchone()
        conn.close()
        return dict(row) if row else None

    def save(self, titulo, genero, duracao_min, diretor, elenco):
        conn = get_connection()
        cursor = conn.execute(
            "INSERT INTO filme (titulo, genero, duracao_min, diretor, elenco) VALUES (?,?,?,?,?)",
            (titulo, genero, duracao_min, diretor, elenco)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id


class SessaoRepository:
    def find_by_cinema(self, cinema_id):
        conn = get_connection()
        rows = conn.execute("""
            SELECT s.id, s.data_hora, s.sala,
                   f.titulo AS filme_titulo, f.duracao_min,
                   c.nome AS cinema_nome
            FROM sessao s
            JOIN filme f ON f.id = s.filme_id
            JOIN cinema c ON c.id = s.cinema_id
            WHERE s.cinema_id = ?
            ORDER BY s.data_hora
        """, (cinema_id,)).fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def save(self, cinema_id, filme_id, data_hora, sala):
        conn = get_connection()
        cursor = conn.execute(
            "INSERT INTO sessao (cinema_id, filme_id, data_hora, sala) VALUES (?,?,?,?)",
            (cinema_id, filme_id, data_hora, sala)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def check_conflict(self, cinema_id, sala, data_hora, duracao_min):
        """Verifica conflito de horário: intervalo mínimo de 30min após o fim da sessão anterior."""
        conn = get_connection()
        rows = conn.execute("""
            SELECT s.data_hora, f.duracao_min
            FROM sessao s JOIN filme f ON f.id = s.filme_id
            WHERE s.cinema_id = ? AND s.sala = ?
        """, (cinema_id, sala)).fetchall()
        conn.close()
        from datetime import datetime, timedelta
        nova = datetime.fromisoformat(data_hora)
        for r in rows:
            existente = datetime.fromisoformat(r['data_hora'])
            fim_existente = existente + timedelta(minutes=r['duracao_min'] + 30)
            fim_nova = nova + timedelta(minutes=duracao_min + 30)
            if not (nova >= fim_existente or existente >= fim_nova):
                return True
        return False


class PublicoRepository:
    def save(self, sessao_id, data, publico):
        conn = get_connection()
        conn.execute(
            "INSERT INTO registro_publico (sessao_id, data, publico) VALUES (?,?,?)",
            (sessao_id, data, publico)
        )
        conn.commit()
        conn.close()

    def total_por_sessao(self, sessao_id):
        conn = get_connection()
        row = conn.execute(
            "SELECT COALESCE(SUM(publico),0) AS total FROM registro_publico WHERE sessao_id = ?",
            (sessao_id,)
        ).fetchone()
        conn.close()
        return row['total']

    def total_por_cinema(self, cinema_id):
        conn = get_connection()
        row = conn.execute("""
            SELECT COALESCE(SUM(rp.publico),0) AS total
            FROM registro_publico rp
            JOIN sessao s ON s.id = rp.sessao_id
            WHERE s.cinema_id = ?
        """, (cinema_id,)).fetchone()
        conn.close()
        return row['total']

    def total_por_filme(self, filme_id):
        conn = get_connection()
        row = conn.execute("""
            SELECT COALESCE(SUM(rp.publico),0) AS total
            FROM registro_publico rp
            JOIN sessao s ON s.id = rp.sessao_id
            WHERE s.filme_id = ?
        """, (filme_id,)).fetchone()
        conn.close()
        return row['total']


class CinemaRepository:
    def find_all(self):
        conn = get_connection()
        rows = conn.execute("SELECT * FROM cinema ORDER BY nome").fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def find_by_id(self, cinema_id):
        conn = get_connection()
        row = conn.execute("SELECT * FROM cinema WHERE id = ?", (cinema_id,)).fetchone()
        conn.close()
        return dict(row) if row else None


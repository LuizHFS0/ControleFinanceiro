import sqlite3

def conectar():
    return sqlite3.connect("dados.db")

def criarTabelas(conn):
    cursor = conn.cursor()

    # Aqui vai as tabelas do banco de dados

    cursor.execute("""CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,
        valor REAL NOT NULL,
        categoria TEXT NOT NULL,
        descricao TEXT,
        data TEXT NOT NULL
    )""")

    conn.commit()
import sqlite3

def conectar():
    return sqlite3.connect("dados.db")

def criarTabelas(conn):
    cursor = conn.cursor()

    # Aqui vai as tabelas do banco de dados

    conn.commit()
import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3
import time

from utils.cores import CORES

def buscarDadosTransacoesDB(tipo):
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()

    # Consulta
    cursor.execute("SELECT id, tipo, REPLACE(printf('R$%.2f', valor), '.', ',') as valor, categoria, strftime('%d/%m/%Y', data) FROM transacoes WHERE tipo = ?", (tipo,))
    dados = cursor.fetchall()
    conn.close()
    return dados


def atualizarTabelaTransacoesDespesas(tela, termo=""):
    # Limpar a tabela antes de atualizar
    for item in tela.tabelaDespesa.get_children():
        tela.tabelaDespesa.delete(item)

    # Consulta SQL para buscar transações com base no termo de pesquisa
    cursor = tela.conn.cursor()

    resultados = buscarDadosTransacoesDB("Despesa")
    for row in resultados:
        tela.tabelaDespesa.insert("", "end", values=row)

def atualizarTabelaTransacoesReceita(tela, termo=""):
    # Limpar a tabela antes de atualizar
    for item in tela.tabelaEntrada.get_children():
        tela.tabelaEntrada.delete(item)

    # Consulta SQL pela função de busca no banco de dados

    resultados = buscarDadosTransacoesDB("Receita")
    for dados in resultados:
        tela.tabelaEntrada.insert("", "end", values=dados)

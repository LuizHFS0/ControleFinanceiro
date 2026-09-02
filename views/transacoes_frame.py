import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

from utils.cores import CORES
from dao.transacaoDAO import atualizarTabelaTransacoesDespesas, atualizarTabelaTransacoesReceita

class TransacoesFrame(ctk.CTkFrame):
    def __init__(self, parent, conn):
        super().__init__(parent)
        self.conn = conn
        self.configure(fg_color=CORES["fundo"])

        # Frame cabeçalho 
        frameCabecalho = ctk.CTkFrame(self, height=175, corner_radius=10, fg_color=CORES["fundo"])
        frameCabecalho.pack(fill="x")         
        frameCabecalho.pack_propagate(False)  

        # Frame final   
        frameFinal = ctk.CTkFrame(self, corner_radius=10, fg_color=CORES["fundo"])
        frameFinal.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        ctk.CTkLabel(frameCabecalho, text="Transações", font=("Arial", 24, "bold"), text_color=CORES["texto"]).pack(pady=20, anchor="w", padx=20)

        # Linha com os botões (esquerda) e o visor (direita)
        frameLinhaAcoes = ctk.CTkFrame(frameCabecalho, fg_color="transparent")
        frameLinhaAcoes.pack(fill="x", padx=20)

        # Botões para adicionar entrada e saída
        btn_adicionarEntrada = ctk.CTkButton(frameLinhaAcoes, text="Nova Entrada", font=("Arial", 16, "bold"), 
                                            fg_color=CORES["entrada"], hover_color=CORES["entradaHover"], width=125)
        btn_adicionarEntrada.pack(side="left")

        btn_adicionarSaida = ctk.CTkButton(frameLinhaAcoes, text="Nova Saída", font=("Arial", 16, "bold"),
                                            fg_color=CORES["despesa"], hover_color=CORES["despesaHover"], width=125)
        btn_adicionarSaida.pack(side="left", padx=(10, 0))

        # Visor para ver o total em conta
        self.visorValorTotal = ctk.CTkFrame(frameLinhaAcoes, width=150, height=80, corner_radius=10, fg_color=CORES["card"])
        self.visorValorTotal.pack(side="right")
        self.visorValorTotal.pack_propagate(False)

        # - Dentro do visor, colocar o valor total em conta
        ctk.CTkLabel(self.visorValorTotal, text="Total em Conta:",
                    font=("Arial", 12), text_color=CORES["texto_secundario"]).pack(anchor="w", padx=8, pady=(10, 0))
        self.labelValorTotal = ctk.CTkLabel(self.visorValorTotal, text="R$ 0,00",
                                            font=("Arial", 24, "bold"), text_color=CORES["texto"])
        self.labelValorTotal.pack(anchor="w", padx=8, pady=(2, 0))

        # Configura o grid do frameFinal para expandir igualmente
        frameFinal.grid_columnconfigure(0, weight=1, uniform="tabelas")
        frameFinal.grid_columnconfigure(1, weight=1, uniform="tabelas")
        frameFinal.grid_rowconfigure(0, weight=1)
        
        style = ttk.Style()
        style.theme_use("clam")  

        # Corpo da tabela
        style.configure(
            "Custom.Treeview",
            background=CORES["card"],
            fieldbackground=CORES["card"],
            foreground=CORES["texto"],
            borderwidth=0,
            relief="flat",
            rowheight=28
        )
        style.map(
            "Custom.Treeview",
            background=[("selected", CORES["fundo_secundario"])],
            foreground=[("selected", CORES["texto"])]
        )

        style.configure(
            "Custom.Treeview.Heading",
            background=CORES["fundo_secundario"],
            foreground=CORES["texto"],
            borderwidth=0,
            relief="flat",
            font=("Arial", 12, "bold")
        )
        style.map(
            "Custom.Treeview.Heading",
            background=[("active", CORES["card"])] 
        )

        style.layout("Custom.Treeview", [
            ("Custom.Treeview.treearea", {"sticky": "nswe"})
        ])

        # Frame Tabela Entradas
        frameTabelaEntradas = ctk.CTkFrame(frameFinal, corner_radius=10, fg_color=CORES["card"])
        frameTabelaEntradas.grid(row=0, column=0, padx=(0, 5), pady=0, sticky="nsew")

        # Tabela de Entradas

        colunasEntradas = ("id", "tipo", "valor", "categoria", "data")

        self.tabelaEntrada = ttk.Treeview(frameTabelaEntradas, columns=colunasEntradas, style="Custom.Treeview", show="headings")

        self.tabelaEntrada.heading("id", text="ID")
        self.tabelaEntrada.heading("tipo", text="Tipo") 
        self.tabelaEntrada.heading("valor", text="Valor")
        self.tabelaEntrada.heading("categoria", text="Categoria")
        self.tabelaEntrada.heading("data", text="Data")

        self.tabelaEntrada.column("id", width=40, anchor="center", stretch=True)
        self.tabelaEntrada.column("tipo", width=90, anchor="center", stretch=True)
        self.tabelaEntrada.column("valor", width=90, anchor="center", stretch=True)
        self.tabelaEntrada.column("categoria", width=130, anchor="center", stretch=True)
        self.tabelaEntrada.column("data", width=90, anchor="center", stretch=True)

        # Colocar aqui a função que atualiza a tabela com os dados do banco de dados

        self.tabelaEntrada.pack(pady=10, padx=10, fill="both", expand=True)

        # Frame Tabela Despesas
        frameTabelaDespesas = ctk.CTkFrame(frameFinal, corner_radius=10, fg_color=CORES["card"])
        frameTabelaDespesas.grid(row=0, column=1, padx=(5, 0), pady=0, sticky="nsew")

        # Tabela de despesas

        colunasDespesa = ("id", "tipo", "valor", "categoria", "data")
        
        self.tabelaDespesa = ttk.Treeview(frameTabelaDespesas, columns=colunasDespesa, style="Custom.Treeview", show="headings")

        self.tabelaDespesa.heading("id", text="ID")
        self.tabelaDespesa.heading("tipo", text="Tipo") 
        self.tabelaDespesa.heading("valor", text="Valor")
        self.tabelaDespesa.heading("categoria", text="Categoria")
        self.tabelaDespesa.heading("data", text="Data")

        self.tabelaDespesa.column("id", width=40, anchor="center", stretch=True)
        self.tabelaDespesa.column("tipo", width=90, anchor="center", stretch=True)
        self.tabelaDespesa.column("valor", width=90, anchor="center", stretch=True)
        self.tabelaDespesa.column("categoria", width=130, anchor="center", stretch=True)
        self.tabelaDespesa.column("data", width=90, anchor="center", stretch=True)

        atualizarTabelaTransacoesReceita(self, "")
        atualizarTabelaTransacoesDespesas(self, "")

        self.tabelaDespesa.pack(pady=10, padx=10, fill="both", expand=True)
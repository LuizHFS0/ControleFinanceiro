import customtkinter as ctk

from utils.cores import CORES

class DashboardFrame(ctk.CTkFrame):
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

        ctk.CTkLabel(frameCabecalho, text="Dashboard", font=("Arial", 24, "bold"), text_color=CORES["texto"]).pack(pady=20, anchor="w", padx=20)

        # Linha com os botões (esquerda) e o visor (direita)
        frameLinhaAcoes = ctk.CTkFrame(frameCabecalho, fg_color="transparent")
        frameLinhaAcoes.pack(fill="x", padx=20)

        # Botões para adicionar entrada e saída
        btn_adicionarEntrada = ctk.CTkButton(frameLinhaAcoes, text="Pagar Despesa", font=("Arial", 16, "bold"), 
                                            fg_color=CORES["entrada"], hover_color=CORES["entradaHover"], width=125)
        btn_adicionarEntrada.pack(side="left")

        btn_adicionarSaida = ctk.CTkButton(frameLinhaAcoes, text="Nova Despesa", font=("Arial", 16, "bold"),
                                            fg_color=CORES["despesa"], hover_color=CORES["despesaHover"], width=125)
        btn_adicionarSaida.pack(side="left", padx=(10, 0))

        # Visor para ver o total em conta
        self.visorValorTotal = ctk.CTkFrame(frameLinhaAcoes, width=150, height=80, corner_radius=10, fg_color=CORES["card"])
        self.visorValorTotal.pack(side="right")
        self.visorValorTotal.pack_propagate(False)

        # - Dentro do visor, colocar o valor total em conta
        ctk.CTkLabel(self.visorValorTotal, text="Total de Despesas:",
                    font=("Arial", 12), text_color=CORES["texto_secundario"]).pack(anchor="w", padx=8, pady=(10, 0))
        self.labelValorTotal = ctk.CTkLabel(self.visorValorTotal, text="R$ 0,00",
                                            font=("Arial", 24, "bold"), text_color=CORES["texto"])
        self.labelValorTotal.pack(anchor="w", padx=8, pady=(2, 0))
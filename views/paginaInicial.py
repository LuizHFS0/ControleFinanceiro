import customtkinter as ctk 

from utils.cores import CORES
from views.dashboard_frame import DashboardFrame
from views.transacoes_frame import TransacoesFrame
from views.despesas_frame import DespesasFrame


class App(ctk.CTk):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.title("Sistema de Controle Financeiro")
        self.geometry("1300x800")
        self.configure(fg_color=CORES["fundo"])

        # Barra lateral
        self.sidebar = ctk.CTkFrame(self, width=275, corner_radius=0, fg_color=CORES["fundo_secundario"])
        self.sidebar.pack(side="left", fill="y")

        tituloLateral = ctk.CTkLabel(self.sidebar, text="Controle Financeiro", font=("Arial", 20, "bold"), text_color=CORES["texto"])
        tituloLateral.place(relx=0.5, y=35, anchor="center")

        # Container onde os frames vão ficar empilhados
        self.container = ctk.CTkFrame(self, corner_radius=0, fg_color=CORES["fundo"])
        self.container.pack(side="right", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Registro dos frames disponíveis
        self.frames = {}
        for FrameClass in (DashboardFrame, TransacoesFrame, DespesasFrame):
            frame = FrameClass(self.container, self.conn)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Botões
        btns = [
            ("Dashboard", 35, 100, "DashboardFrame"),
            ("Transações", 35, 150, "TransacoesFrame"),
            ("Despesas", 35, 200, "DespesasFrame"),
        ]

        for nome, x, y, frame_key in btns:
            btn = ctk.CTkButton(
                self.sidebar, text=nome, font=("Arial", 16, "bold"),
                fg_color=CORES["fundo_secundario"], hover_color=CORES["fundo"],
                text_color=CORES["texto"], anchor="w", width=200, height=40,
                command=lambda key=frame_key: self.mostrar_frame(key)
            )
            btn.place(x=x, y=y)

        self.mostrar_frame("DashboardFrame")

    def mostrar_frame(self, nome_frame):
        frame = self.frames[nome_frame]
        frame.tkraise()
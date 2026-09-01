import customtkinter as ctk

class RelatorioFrame(ctk.CTkFrame):
    def __init__(self, parent, conn):
        super().__init__(parent)
        self.conn = conn
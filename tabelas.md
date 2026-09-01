

        # Tabela de despesas

        colunasDespesa = ("id", "tipo", "valor", "categoria", "data")
        
        tabelaDespesa = ttk.Treeview(self, columns=colunasDespesa, show="headings")

        tabelaDespesa.heading("id", text="ID")
        tabelaDespesa.heading("tipo", text="Tipo") 
        tabelaDespesa.heading("valor", text="Valor")
        tabelaDespesa.heading("categoria", text="Categoria")
        tabelaDespesa.heading("data", text="Data")

        tabelaDespesa.column("id", width=50, anchor="center", stretch=False)
        tabelaDespesa.column("tipo", width=100, anchor="center", stretch=False)
        tabelaDespesa.column("valor", width=100, anchor="center", stretch=False)
        tabelaDespesa.column("categoria", width=150, anchor="center", stretch=False)
        tabelaDespesa.column("data", width=100, anchor="center", stretch=False)

        # Colocar aqui a função que atualiza a tabela com os dados do banco de dados

        tabelaDespesa.pack(pady=200, padx=20, fill="both", expand=True)
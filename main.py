from views.paginaInicial import App
from database.db import conectar, criarTabelas

def main():
    conn = conectar() # Cria a conexão com o banco 
    criarTabelas(conn) # Verifica se tem alguma tabela nova pra criar, se não, não acontece nada

    app = App(conn) # Inicia o aplicativo desktop 
    app.mainloop() # Deixa o sistema funcionando até fechar a janela

    conn.close() # Fecha o bando de dados após fechar o aplicativo

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from banco import *

# Criação da janela principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Tela de Entrada de Dados")
        self.resizable(False, False)

        # Fonte customizada
        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")

        # Título
        self.label_title = tk.Label(self, text="Formulário de Entrada", font=title_font)
        self.label_title.pack(pady=20)

        # Entrada 1 (Usuário)
        self.label_entry1 = tk.Label(self, text="Usuário:")
        self.label_entry1.pack(pady=5)
        self.entry1 = tk.Entry(self, width=40)
        self.entry1.pack(pady=5)

        # Entrada 2 (Senha)
        self.label_entry2 = tk.Label(self, text="Senha:")
        self.label_entry2.pack(pady=5)
        self.entry2 = tk.Entry(self, width=40, show="*")  # Ocultando a senha
        self.entry2.pack(pady=5)

        # Botões
        self.button1 = tk.Button(self, text="Login", command=self.autenticacao, width=15, bg="#4CAF50", fg="white")
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self, text="Botão 2", command=self.action_button2, width=15, bg="#2196F3", fg="white")
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self, text="Botão 3", command=self.action_button3, width=15, bg="#f44336", fg="white")
        self.button3.pack(pady=10)

    # Funções dos botões
    def autenticação(self):
        # Conectando ao banco de dados
        conn, cursor = cb()
        if conn is not None and cursor is not None:
            try:
                # Obtendo dados das entradas
                usuario = self.entry1.get()
                senha = self.entry2.get()

                # Consulta SQL para buscar a senha
                sql = "SELECT senha FROM tbl_usuarios WHERE username = %s"
                
                # Executando a consulta com segurança contra SQL Injection
                cursor.execute(sql, (usuario,))
                
                # Obtendo o resultado da consulta
                resultado = cursor.fetchone()  # Captura uma única linha

                if resultado:
                    senha_bd = resultado[0]  # A senha está no primeiro índice do resultado
                    if senha == senha_bd:
                        from tela_principal import MainApp

                        MainApp()
                    else:
                        print("Senha incorreta!")
                else:
                    print("Usuário não encontrado!")

            except Error as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
            finally:
                # Fechando a conexão com o banco de dados
                fc(conn, cursor)


    def action_button2(self):
        print("Botão 2 pressionado!")

    def action_button3(self):
        print("Botão 3 pressionado!")

# Inicializando a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()

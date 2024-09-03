import tkinter as tk
from tkinter import messagebox
import sqlite3
from banco import banco

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        
        # Inicializa o banco de dados
        self.db = banco()
        
        # Criação dos widgets da tela de login
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(pady=20)

        self.label_usuario = tk.Label(self.frame_principal, text="Usuário:")
        self.label_usuario.pack(anchor='w', padx=10, pady=5)
        
        self.entry_usuario = tk.Entry(self.frame_principal)
        self.entry_usuario.pack(fill='x', padx=10, pady=5)
        
        self.label_senha = tk.Label(self.frame_principal, text="Senha:")
        self.label_senha.pack(anchor='w', padx=10, pady=5)
        
        self.entry_senha = tk.Entry(self.frame_principal, show="*")
        self.entry_senha.pack(fill='x', padx=10, pady=5)
        
        self.botao_login = tk.Button(self.frame_principal, text="Login", command=self.verificar_login)
        self.botao_login.pack(pady=20)
        
    def verificar_login(self):
        self.usuario = self.entry_usuario.get()
        self.senha = self.entry_senha.get()
        
        banco_con = banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("SELECT * FROM usuario WHERE usuario = ? AND senha = ?", (self.usuario, self.senha))
            resultado = c.fetchone()
            c.close()
            
            if resultado:
                self.abrir_menu_inicial()
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca do usuário: {str(e)}")
    
    def abrir_menu_inicial(self):
        # Oculta a janela de login e abre a tela principal
        self.root.withdraw()
        from menuinicial import MenuInicial
        app = MenuInicial(self.root)
        self.root.state("zoomed")
        self.root.mainloop()

# Inicializa a aplicação
root = tk.Tk()
app = TelaLogin(root)
root.state("zoomed")
root.mainloop()

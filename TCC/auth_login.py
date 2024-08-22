import customtkinter as ctk
from conecta import *
from PIL import Image, ImageTk
import cv2

class Login(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.titulo = ctk.CTkLabel(self, text="Login", font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo.pack(pady=20)

        self.usuarioLabel = ctk.CTkLabel(self, text="Usuário")
        self.usuarioLabel.pack()

        self.usuario = ctk.CTkEntry(self, width=250)
        self.usuario.pack(pady=10)

        self.senhaLabel = ctk.CTkLabel(self, text="Senha")
        self.senhaLabel.pack()

        self.senha = ctk.CTkEntry(self, width=250, show="*")
        self.senha.pack(pady=10)

        self.entrar = ctk.CTkButton(self, text="Entrar", command=self.verificaSenha)
        self.entrar.pack(pady=10)

        self.cadastrar = ctk.CTkButton(self, text="Cadastrar", command=self.abrir_tela_cadastro)
        self.cadastrar.pack()

        self.esqueci_senha = ctk.CTkButton(self, text="Esqueci minha senha", command=self.esqueciSenha)
        self.esqueci_senha.pack(pady=10)

        self.mensagem = ctk.CTkLabel(self, text="")
        self.mensagem.pack()

    def verificaSenha(self):
        from frames_main_frame import DesenhoTela
        usuario = self.usuario.get()
        senha = self.senha.get()
        try:
            cursor = self.master.db.cursor(buffered=True)
            cursor.execute("SELECT usu_senha FROM usuario WHERE usu_usuario = %s", (usuario,))
            resultado = cursor.fetchone()
            if resultado and resultado[0] == senha:
                self.master.current_user = usuario  # Armazena o nome do usuário no master
                self.master.switch_frame(DesenhoTela)
            else:
                self.mensagem.configure(text="Erro na autenticação")
        except mysql.connector.Error as err:
            self.mensagem.configure(text=f"Erro na autenticação: {err}")
        finally:
            cursor.close()  # Garante que o cursor seja fechado

    def abrir_tela_cadastro(self):
        from auth_cadastro import Cadastro  # Importação atrasada para evitar importação circular
        self.master.switch_frame(Cadastro)

    def esqueciSenha(self):
        from auth_esqueci_senha import EsqueciSenha  # Importação atrasada para evitar importação circular
        self.master.switch_frame(EsqueciSenha)

from tkinter import *
import customtkinter as ctk
from conecta import conectar_ao_banco
import cv2 
from PIL import Image,ImageTk
import mysql.connector
from auth_login import Login
from utilidades import *

class EsqueciSenha(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(self)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Redefinir Senha")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome de usuário", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome.pack(side=LEFT)

        self.novaSenhaLabel = Label(self.terceiroContainer, text="Nova Senha", font=self.fontePadrao)
        self.novaSenhaLabel.pack(side=LEFT)

        self.novaSenha = Entry(self.terceiroContainer)
        self.novaSenha["width"] = 30
        self.novaSenha["font"] = self.fontePadrao
        self.novaSenha["show"] = "*"
        self.novaSenha.pack(side=LEFT)

        self.confirmarSenhaLabel = Label(self.quartoContainer, text="Confirmar Nova Senha", font=self.fontePadrao)
        self.confirmarSenhaLabel.pack(side=LEFT)

        self.confirmarSenha = Entry(self.quartoContainer)
        self.confirmarSenha["width"] = 30
        self.confirmarSenha["font"] = self.fontePadrao
        self.confirmarSenha["show"] = "*"
        self.confirmarSenha.pack(side=LEFT)

        self.botaoRedefinir = Button(self.quartoContainer, text="Redefinir", font=("Calibri", "8"), width=12, command=self.redefinir_senha)
        self.botaoRedefinir.pack()

        self.botaoRedefinir = Button(self.quartoContainer, text="Voltar", font=("Calibri", "8"), width=12, command=self.retorno)
        self.botaoRedefinir.pack()


        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def redefinir_senha(self):
        usuario = self.nome.get()
        nova_senha = self.novaSenha.get()
        confirmar_senha = self.confirmarSenha.get()

        if nova_senha != confirmar_senha:
            self.mensagem["text"] = "As senhas não coincidem."
            return

        espaco = contar_espacos(nova_senha)
        quantidade = contar_letras(nova_senha)

        if espaco > 0 or quantidade < 8:
            self.mensagem["text"] = "A senha deve ter pelo menos 8 caracteres e não deve conter espaços."
            return

        cursor = self.master.db.cursor()
        cursor.execute("SELECT usu_nome FROM usuario WHERE usu_nome = %s", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            try:
                cursor.execute("UPDATE usuario SET usu_senha = %s WHERE usu_nome = %s", (nova_senha, usuario))
                self.master.db.commit()
                self.mensagem["text"] = "Senha redefinida com sucesso."
                self.master.switch_frame(Login)
            except mysql.connector.Error as err:
                self.mensagem["text"] = f"Erro ao redefinir senha: {err}"
        else:
            self.mensagem["text"] = "Usuário não encontrado."

    def retorno(self):
        self.master.switch_frame(Login)


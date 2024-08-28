import tkinter as tk
from manutencao import busuarios

class Usuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface do Usuário")  

        # Título centralizado no topo
        self.titulo = tk.Label(root, text="Título Centralizado", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

        # Segunda linha: Label, Entrada e Botão
        self.label1 = tk.Label(root, text="Id:")
        self.label1.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.entrada1 = tk.Entry(root)
        self.entrada1.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.botao1 = tk.Button(root, text="Buscar", command=self.buscar)
        self.botao1.grid(row=1, column=2, padx=10, pady=5)

        # Linhas 3-7: Label à esquerda e Entrada à direita (colspan=2 para entradas)
        self.label2 = tk.Label(root, text="Nome:")
        self.label2.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.entrada2 = tk.Entry(root, width=30)
        self.entrada2.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        self.label3 = tk.Label(root, text="Telefone:")
        self.label3.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.entrada3 = tk.Entry(root, width=30)
        self.entrada3.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        self.label4 = tk.Label(root, text="E-mail:")
        self.label4.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.entrada4 = tk.Entry(root, width=30)
        self.entrada4.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        self.label5 = tk.Label(root, text="Usuário:")
        self.label5.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        self.entrada5 = tk.Entry(root, width=30)
        self.entrada5.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        self.label6 = tk.Label(root, text="Senha:")
        self.label6.grid(row=6, column=0, padx=10, pady=5, sticky="e")

        self.entrada6 = tk.Entry(root, width=30, show="*")
        self.entrada6.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        # Botões na linha 7
        self.botaoEnviar = tk.Button(root, text="Inserir", width=20, command=self.inserir)
        self.botaoEnviar.grid(row=7, column=0, padx=10, pady=5)

        self.botaoAlterar = tk.Button(root, text="Alterar", width=20, command=self.alterar)
        self.botaoAlterar.grid(row=7, column=1, padx=10, pady=5)

        self.botaoExcluir = tk.Button(root, text="Excluir", width=20, command=self.excluir)
        self.botaoExcluir.grid(row=7, column=2, padx=10, pady=5)

        # Configura as colunas para expandirem conforme necessário
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)

    def inserir(self):
        usuario = busuarios(
            nome=self.entrada2.get(),
            telefone=self.entrada3.get(),
            email=self.entrada4.get(),
            usuario=self.entrada5.get(),
            senha=self.entrada6.get()
        )
        mensagem = usuario.insertUser()
        print(mensagem)  # Para verificação, você pode exibir a mensagem em uma label na interface

        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)
        self.entrada3.delete(0, tk.END)
        self.entrada4.delete(0, tk.END)
        self.entrada5.delete(0, tk.END)
        self.entrada6.delete(0, tk.END)

       

    def buscar(self):
        idusuario = self.entrada1.get()
        usuario = busuarios(idusuario=idusuario)
        mensagem = usuario.selectUser()
        if mensagem == "Busca feita com sucesso!":
            self.entrada2.delete(0, tk.END)
            self.entrada2.insert(0, usuario.nome)
            self.entrada3.delete(0, tk.END)
            self.entrada3.insert(0, usuario.telefone)
            self.entrada4.delete(0, tk.END)
            self.entrada4.insert(0, usuario.email)
            self.entrada5.delete(0, tk.END)
            self.entrada5.insert(0, usuario.usuario)
            self.entrada6.delete(0, tk.END)
            self.entrada6.insert(0, usuario.senha)
        print(mensagem)

    def alterar(self):
        usuario = busuarios(
            idusuario=self.entrada1.get(),
            nome=self.entrada2.get(),
            telefone=self.entrada3.get(),
            email=self.entrada4.get(),
            usuario=self.entrada5.get(),
            senha=self.entrada6.get()
        )
        mensagem = usuario.updateUser()
        print(mensagem)

    def excluir(self):
        usuario = busuarios(idusuario=self.entrada1.get())
        mensagem = usuario.deleteUser()
        print(mensagem)


# Inicializa a aplicação
root = tk.Tk()
app = Usuario(root)
root.mainloop()

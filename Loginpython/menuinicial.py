import tkinter as tk

class MenuInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Inicial")

        # Container principal
        self.container1 = tk.Frame(root)
        self.container1.pack()

        # Criação dos 4 botões, um ao lado do outro
        self.botao_usuario = tk.Button(self.container1, text="Usuário", command=self.abrir_usuario)
        self.botao_usuario.grid(row=0, column=0, padx=10, pady=10)

        self.botao_2 = tk.Button(self.container1, text="Cidades", command=self.abrir_cidade)
        self.botao_2.grid(row=0, column=1, padx=10, pady=10)

        self.botao_3 = tk.Button(self.container1, text="Clientes", command=self.abrir_clientes)
        self.botao_3.grid(row=0, column=2, padx=10, pady=10)

        self.botao_4 = tk.Button(self.container1, text="Fechar", command=self.root.quit)
        self.botao_4.grid(row=0, column=3, padx=10, pady=10)

    def abrir_usuario(self):
        from Loginpython.paginausuario1 import Usuario
        # Cria uma nova janela e instancia a classe Usuario
        nova_janela = tk.Toplevel(self.root)
        app = Usuario(nova_janela)

    def abrir_cidade(self):
        from paginacidade1 import Cidade
        # Cria uma nova janela e instancia a classe Cidade
        nova_janela = tk.Toplevel(self.root)
        app = Cidade(nova_janela)

    def abrir_clientes(self):
        from Loginpython.paginaclientes1 import Clientes
        # Cria uma nova janela e instancia a classe Cidade
        nova_janela = tk.Toplevel(self.root)
        app = Clientes(nova_janela)

# Inicializa a aplicação
root = tk.Tk()
app = MenuInicial(root)
root.state("zoomed")
root.mainloop()

import tkinter as tk
from tkinter import Menu

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
        from paginausuario1 import Usuario
        # Cria uma nova janela e instancia a classe Usuario
        nova_janela = tk.Toplevel(self.root)
        app = Usuario(nova_janela)

    def abrir_cidade(self):
        from paginacidade1 import Cidade
        # Cria uma nova janela e instancia a classe Cidade
        nova_janela = tk.Toplevel(self.root)
        app = Cidade(nova_janela)

    def abrir_clientes(self):
        from paginaclientes1 import Clientes
        # Cria uma nova janela e instancia a classe Clientes
        nova_janela = tk.Toplevel(self.root)
        app = Clientes(nova_janela)

# Inicializa a aplicação
root = tk.Tk()

# Criação da instância da interface principal
app = MenuInicial(root)

# Criação da barra de menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

# Aqui utilizamos lambda para chamar os métodos da instância `app`
filemenu.add_command(label="Cidade", command=app.abrir_cidade)
filemenu.add_command(label="Clientes", command=app.abrir_clientes)
filemenu.add_command(label="Usuario", command=app.abrir_usuario)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Adiciona o menu "File" na barra de menus
menubar.add_cascade(label="File", menu=filemenu)

# Configura a janela principal para usar a barra de menu
root.config(menu=menubar)

# Configura a janela principal para abrir maximizada
root.state("zoomed")
root.mainloop()

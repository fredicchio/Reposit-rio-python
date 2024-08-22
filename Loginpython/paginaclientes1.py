import tkinter as tk

class Clientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Clientes")  

        # Título centralizado no topo
        self.titulo = tk.Label(root, text="Gerenciamento de Clientes", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

        # Linha 1: Nome
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entrada_nome = tk.Entry(root, width=30)
        self.entrada_nome.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Linha 2: Email
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entrada_email = tk.Entry(root, width=30)
        self.entrada_email.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Linha 3: Telefone
        self.label_telefone = tk.Label(root, text="Telefone:")
        self.label_telefone.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.entrada_telefone = tk.Entry(root, width=30)
        self.entrada_telefone.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Botões na parte inferior
        self.botao_buscar = tk.Button(root, text="Buscar", command=self.buscar)
        self.botao_buscar.grid(row=4, column=0, padx=10, pady=5)

        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.adicionar)
        self.botao_adicionar.grid(row=4, column=1, padx=10, pady=5)

        self.botao_excluir = tk.Button(root, text="Excluir", command=self.excluir)
        self.botao_excluir.grid(row=4, column=2, padx=10, pady=5)

        self.botao_alterar = tk.Button(root, text="Alterar", command=self.alterar)
        self.botao_alterar.grid(row=4, column=3, padx=10, pady=5)

        # Configura as colunas para expandirem conforme necessário
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)

    def buscar(self):
        dados = {
            "Nome": self.entrada_nome.get(),
            "Email": self.entrada_email.get(),
            "Telefone": self.entrada_telefone.get()
        }
        print("Buscar:", dados)

    def adicionar(self):
        dados = {
            "Nome": self.entrada_nome.get(),
            "Email": self.entrada_email.get(),
            "Telefone": self.entrada_telefone.get()
        }
        print("Adicionar:", dados)

    def excluir(self):
        dados = {
            "Nome": self.entrada_nome.get(),
            "Email": self.entrada_email.get(),
            "Telefone": self.entrada_telefone.get()
        }
        print("Excluir:", dados)

    def alterar(self):
        dados = {
            "Nome": self.entrada_nome.get(),
            "Email": self.entrada_email.get(),
            "Telefone": self.entrada_telefone.get()
        }
        print("Alterar:", dados)

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = Clientes(root)
    root.mainloop()

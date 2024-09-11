import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from manutencao import bclientes, populate_treeview

class Clientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Clientes")  

        # Título centralizado no topo
        self.titulo = tk.Label(root, text="Gerenciamento de Clientes", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=5, pady=10, sticky="n")

        # Linha 1: ID do Cliente
        self.label_id = tk.Label(root, text="ID Cliente:")
        self.label_id.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entrada_id = tk.Entry(root, width=10)
        self.entrada_id.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Linha 2: Nome
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entrada_nome = tk.Entry(root, width=30)
        self.entrada_nome.grid(row=2, column=1, columnspan=4, padx=10, pady=5, sticky="ew")

        # Linha 3: Email
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.entrada_email = tk.Entry(root, width=30)
        self.entrada_email.grid(row=3, column=1, columnspan=4, padx=10, pady=5, sticky="ew")

        # Linha 4: Telefone
        self.label_telefone = tk.Label(root, text="Telefone:")
        self.label_telefone.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.entrada_telefone = tk.Entry(root, width=30)
        self.entrada_telefone.grid(row=4, column=1, columnspan=4, padx=10, pady=5, sticky="ew")

        # Linha 5: Cidade
        self.label_cidade = tk.Label(root, text="Cidade:")
        self.label_cidade.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.lista_cidades = tk.Listbox(root, width=30, height=5)
        self.lista_cidades.grid(row=5, column=1, columnspan=4, padx=10, pady=5, sticky="ew")
        self.carregarCidades()

        # Botões na parte inferior
        self.botao_buscar = tk.Button(root, text="Buscar", command=self.buscar)
        self.botao_buscar.grid(row=6, column=0, padx=10, pady=5)

        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.adicionar)
        self.botao_adicionar.grid(row=6, column=1, padx=10, pady=5)

        self.botao_excluir = tk.Button(root, text="Excluir", command=self.excluir)
        self.botao_excluir.grid(row=6, column=2, padx=10, pady=5)

        self.botao_alterar = tk.Button(root, text="Alterar", command=self.alterar)
        self.botao_alterar.grid(row=6, column=3, padx=10, pady=5)

        self.botao_voltar = tk.Button(root, text="Voltar", command=self.root.destroy)
        self.botao_voltar.grid(row=6, column=4, padx=10, pady=5)

        # Configura as colunas para expandirem conforme necessário
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)
        root.grid_columnconfigure(4, weight=1)

        self.columns = ('ID', 'NOME', 'TELEFONE', 'EMAIL', 'CIDADE')
        self.treeview = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.treeview.heading(col, text=col)

        self.treeview.grid(row=8, column=0, columnspan=3, sticky="nsew")

        # Chama o método de refresh ao iniciar
        self.refresh_treeview()

    def refresh_treeview(self):
        data = bclientes().selectall()
        if not data:
            print("Nenhum dado encontrado ou ocorreu um erro ao buscar os dados.")
        else:
            populate_treeview(self.treeview, data)

    def carregarCidades(self):
        cliente = bclientes()
        cidades = cliente.getAllCities()
        self.lista_cidades.delete(0, tk.END)
        for cidade in cidades:
            self.lista_cidades.insert(tk.END, f"{cidade[0]} - {cidade[1]}")

    def buscar(self):
        idcliente = self.entrada_id.get()
        if not idcliente:
            messagebox.showwarning("Aviso", "Por favor, insira o ID do cliente.")
            return

        try:
            idcliente = int(idcliente)
        except ValueError:
            messagebox.showerror("Erro", "O ID do cliente deve ser um número inteiro.")
            return

        cliente = bclientes(idcliente=idcliente)
        resultado = cliente.selectClient()
        if "Ocorreu um erro" in resultado:
            messagebox.showerror("Erro", resultado)
        else:
            self.entrada_nome.delete(0, tk.END)
            self.entrada_nome.insert(0, cliente.nome)
            self.entrada_email.delete(0, tk.END)
            self.entrada_email.insert(0, cliente.email)
            self.entrada_telefone.delete(0, tk.END)
            self.entrada_telefone.insert(0, cliente.telefone)

            # Seleciona a cidade na lista de cidades
            cidade_index = self.find_city_index(cliente.codcidade)
            if cidade_index is not None:
                self.lista_cidades.selection_set(cidade_index)
                self.lista_cidades.activate(cidade_index)
        self.refresh_treeview()

    def find_city_index(self, codcidade):
        for index, item in enumerate(self.lista_cidades.get(0, tk.END)):
            if item.startswith(f"{codcidade}"):
                return index
        return None

    def adicionar(self):
        nome = self.entrada_nome.get()
        email = self.entrada_email.get()
        telefone = self.entrada_telefone.get()
        cidade = self.lista_cidades.get(tk.ACTIVE).split()[0]  # Pega o código da cidade selecionada

        if not nome or not email or not telefone or not cidade:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        cliente = bclientes(nome=nome, email=email, telefone=telefone, codcidade=cidade)
        resultado = cliente.insertClient()
        messagebox.showinfo("Resultado", resultado)
        self.carregarCidades()  # Atualiza a lista de cidades após adição
        self.refresh_treeview()

    def excluir(self):
        idcliente = self.entrada_id.get()
        if not idcliente:
            messagebox.showwarning("Aviso", "Por favor, insira o ID do cliente.")
            return

        try:
            idcliente = int(idcliente)
        except ValueError:
            messagebox.showerror("Erro", "O ID do cliente deve ser um número inteiro.")
            return

        cliente = bclientes(idcliente=idcliente)
        resultado = cliente.deleteClient()
        messagebox.showinfo("Resultado", resultado)
        self.carregarCidades()  # Atualiza a lista de cidades após exclusão
        self.refresh_treeview()

    def alterar(self):
        idcliente = self.entrada_id.get()
        nome = self.entrada_nome.get()
        email = self.entrada_email.get()
        telefone = self.entrada_telefone.get()
        cidade = self.lista_cidades.get(tk.ACTIVE).split()[0]  # Pega o código da cidade selecionada

        if not idcliente or not nome or not email or not telefone or not cidade:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            idcliente = int(idcliente)
            
        except ValueError:
            messagebox.showerror("Erro", "O ID do cliente deve ser um número inteiro.")
            return

        cliente = bclientes(idcliente=idcliente, nome=nome, email=email, telefone=telefone, codcidade=cidade)
        resultado = cliente.updateClient()
        messagebox.showinfo("Resultado", resultado)
        self.carregarCidades()  # Atualiza a lista de cidades após alteração
        self.refresh_treeview()

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = Clientes(root)
    root.mainloop()

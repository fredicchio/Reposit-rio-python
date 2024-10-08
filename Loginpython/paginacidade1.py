import tkinter as tk
from tkinter import ttk
from manutencao import bcidades, populate_treeview

class Cidade:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Cidades")  

        # Título centralizado no topo
        self.titulo = tk.Label(root, text="Gerenciamento de Cidades", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

        # Linha 1: Código da Cidade
        self.label_codcidade = tk.Label(root, text="Código da Cidade:")
        self.label_codcidade.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entrada_codcidade = tk.Entry(root, width=30)
        self.entrada_codcidade.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Linha 2: Cidade
        self.label_cidade = tk.Label(root, text="Cidade:")
        self.label_cidade.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entrada_cidade = tk.Entry(root, width=30)
        self.entrada_cidade.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Linha 4: UF
        self.label_uf = tk.Label(root, text="UF:")
        self.label_uf.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.entrada_uf = tk.Entry(root, width=30)
        self.entrada_uf.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Botões na parte inferior
        self.botao_buscar = tk.Button(root, text="Buscar", command=self.buscar)
        self.botao_buscar.grid(row=5, column=0, padx=10, pady=5)

        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.adicionar)
        self.botao_adicionar.grid(row=5, column=1, padx=10, pady=5)

        self.botao_excluir = tk.Button(root, text="Excluir", command=self.excluir)
        self.botao_excluir.grid(row=5, column=2, padx=10, pady=5)

        self.botao_alterar = tk.Button(root, text="Alterar", command=self.alterar)
        self.botao_alterar.grid(row=5, column=3, padx=10, pady=5)

        self.botao_voltar = tk.Button(root, text="Voltar", command=self.root.destroy)
        self.botao_voltar.grid(row=5, column=4, padx=10, pady=5)

        # Configura as colunas para expandirem conforme necessário
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)

        self.columns = ('ID', 'CIDADE', 'UF')
        self.treeview = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.grid(row=8, column=0, columnspan=5, sticky="nsew")

        # Chama o método de refresh ao iniciar
        self.refresh_treeview()

    def refresh_treeview(self):
        # Limpa o Treeview antes de adicionar novos dados
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        
        data = bcidades().selectall()
        if not data:
            print("Nenhum dado encontrado ou ocorreu um erro ao buscar os dados.")
        else:
            populate_treeview(self.treeview, data)

    def buscar(self):
        codcidade = self.entrada_codcidade.get()
        cidade = bcidades(codcidade=codcidade)
        mensagem = cidade.selectCity()
        if mensagem == "Busca feita com sucesso!":
            self.entrada_cidade.delete(0, tk.END)
            self.entrada_cidade.insert(0, cidade.nomecid)
            self.entrada_uf.delete(0, tk.END)
            self.entrada_uf.insert(0, cidade.uf)
        print(mensagem)
        self.refresh_treeview()

    def adicionar(self):
        cidade = bcidades(
            nomecid=self.entrada_cidade.get(),
            uf=self.entrada_uf.get()
        )
        mensagem = cidade.insertCity()
        print(mensagem)
        self.refresh_treeview()

        self.entrada_cidade.delete(0, tk.END)
        self.entrada_uf.delete(0, tk.END)

    def excluir(self):
        codcidade = self.entrada_codcidade.get()
        cidade = bcidades(codcidade=codcidade)
        mensagem = cidade.deleteCity()
        print(mensagem)
        self.refresh_treeview()
        self.entrada_codcidade.delete(0, tk.END)
        self.entrada_cidade.delete(0, tk.END)
        self.entrada_uf.delete(0, tk.END)

    def alterar(self):
        cidade = bcidades(
            codcidade=self.entrada_codcidade.get(),
            nomecid=self.entrada_cidade.get(),
            uf=self.entrada_uf.get()
        )
        mensagem = cidade.updateCity()
        print(mensagem)
        self.refresh_treeview()

# Inicializa a aplicação
root = tk.Tk()
app = Cidade(root)
root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
from crude import select_cidades, add_cidade, update_cidade, delete_cidade  # Importando a função de delete

# Classe da janela de adição de cidades
class CidadesADDWindow:
    def __init__(self, master):
        self.window = tk.Toplevel(master)  # Abre uma nova janela separada
        self.window.title("Cadastro de Cidades")

        # Criando entrada para o nome da cidade
        self.entry1 = tk.Entry(self.window)

        # Lista de estados
        estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG",
                   "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR",
                   "RS", "SC", "SE", "SP", "TO"]

        # Criando a Combobox para seleção de estado
        self.combobox = ttk.Combobox(self.window, values=estados, state="readonly")
        self.combobox.set("Selecione um Estado")

        # Posicionando as entradas e a combobox com grid
        self.entry1.grid(row=0, column=1, padx=10, pady=10)
        self.combobox.grid(row=1, column=1, padx=10, pady=10)

        # Adicionando rótulos (labels) para os campos
        tk.Label(self.window, text="Cidade:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.window, text="Estado:").grid(row=1, column=0, padx=10, pady=10)

        # Criando 2 botões: Salvar e Voltar
        tk.Button(self.window, text="Voltar", command=self.window.destroy).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.window, text="Adicionar", command=self.save_data).grid(row=2, column=1, padx=10, pady=10)

    # Função para salvar os dados
    def save_data(self):
        nome = self.entry1.get()
        uf = self.combobox.get()
        if nome and uf != "Selecione um Estado":
            add_cidade(nome, uf)
            self.window.destroy()
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos")


# Classe da janela de edição de cidades
class CidadesEDITWindow:
    def __init__(self, master, cidade_id, nome, uf):
        self.window = tk.Toplevel(master)  # Cria uma nova janela
        self.window.title("Editar Cidade")

        # Campos para editar o nome da cidade e o estado
        self.entry_nome = tk.Entry(self.window)
        self.entry_nome.insert(0, nome)  # Preenche com o nome da cidade atual

        estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG",
                   "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR",
                   "RS", "SC", "SE", "SP", "TO"]

        self.combobox_uf = ttk.Combobox(self.window, values=estados, state="readonly")
        self.combobox_uf.set(uf)  # Preenche com o UF atual

        # Posicionando os campos com grid
        tk.Label(self.window, text="Nome da Cidade:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.window, text="Estado:").grid(row=1, column=0, padx=10, pady=10)
        self.combobox_uf.grid(row=1, column=1, padx=10, pady=10)

        # Botão de salvar alterações
        tk.Button(self.window, text="Salvar", command=lambda: self.save_changes(cidade_id)).grid(row=2, column=0, padx=5, pady=10)
        tk.Button(self.window, text="Excluir", command=lambda: self.delete_cidade(cidade_id)).grid(row=2, column=1, padx=5, pady=10)

    def save_changes(self, cidade_id):
        # Aqui você faria a lógica para salvar os dados editados no banco de dados
        nome_novo = self.entry_nome.get()
        uf_novo = self.combobox_uf.get()

        if nome_novo and uf_novo != "Selecione um Estado":
            update_cidade(cidade_id, nome_novo, uf_novo)  # Atualiza a cidade no banco de dados
            self.window.destroy()
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos corretamente")

    def delete_cidade(self, cidade_id):
        # Função para excluir a cidade
        confirm = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta cidade?")
        if confirm:
            delete_cidade(cidade_id)  # Chama a função de exclusão
            self.window.destroy()
            self.master.reload_data()  # Atualiza o Treeview na janela principal


# Classe da janela principal de visualização de cidades
class CidadesVIEWWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Cidades")

        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Botão de Adicionar
        self.add_button = tk.Button(main_frame, text="Adicionar cidade", command=self.open_add_window)
        self.add_button.pack(side=tk.LEFT)

        # Treeview
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Nome", "UF"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("UF", text="UF")
        self.tree.pack()

        # Campos de pesquisa
        self.create_search_fields(main_frame)

        # Carregar dados iniciais
        self.load_data()

    def load_data(self):
        # Função para carregar os dados do banco no Treeview
        self.tree.delete(*self.tree.get_children())  # Limpa o Treeview antes de carregar novos dados
        cidades = select_cidades()
        for cidade in cidades:
            self.tree.insert("", tk.END, values=cidade)

    def create_search_fields(self, frame):
        # Criação de campos de pesquisa dinâmicos com base nas colunas do Treeview
        tk.Label(frame, text="Pesquisar código:").pack(side=tk.LEFT)
        self.entrycod = tk.Entry(frame)
        self.entrycod.pack(side=tk.LEFT)

        tk.Label(frame, text="Pesquisar pelo nome:").pack(side=tk.LEFT)
        self.entryNome = tk.Entry(frame)
        self.entryNome.pack(side=tk.LEFT)

        tk.Label(frame, text="Pesquisar pelo Estado (abreviação):").pack(side=tk.LEFT)
        self.entryUF = tk.Entry(frame)
        self.entryUF.pack(side=tk.LEFT)

        self.search_button = tk.Button(frame, text="Buscar cidades", command=self.search_button_click)
        self.search_button.pack(side=tk.LEFT)

    def search_button_click(self):
        # Função de busca
        codigo = self.entrycod.get().strip()
        nome = self.entryNome.get().strip()
        uf = self.entryUF.get().strip()

        # Pega todas as cidades
        cidades = select_cidades()

        # Filtrar cidades com base nos critérios de pesquisa
        cidades_filtradas = [
            cidade for cidade in cidades
            if (not codigo or str(cidade[0]) == codigo) and
               (not nome or nome.lower() in cidade[1].lower()) and
               (not uf or cidade[2].lower() == uf.lower())
        ]

        self.tree.delete(*self.tree.get_children())  # Limpa o Treeview
        for cidade in cidades_filtradas:
            self.tree.insert("", tk.END, values=cidade)

    def open_add_window(self):
        # Abre a janela de adicionar cidades
        add_window = CidadesADDWindow(self.root)
        self.root.wait_window(add_window.window)  # Aguarda o fechamento da janela antes de recarregar os dados
        self.reload_data()  # Recarrega os dados após adicionar uma nova cidade

    def reload_data(self):
        # Função para recarregar os dados
        self.load_data()  # Chama a função de carregar dados

    def on_item_double_click(self, event):
        # Função que abre a janela de edição quando um item é clicado duas vezes
        item_id = self.tree.selection()[0]  # Pega o item selecionado
        item_values = self.tree.item(item_id, "values")  # Pega os valores do item selecionado

        cidade_id = item_values[0]  # O primeiro valor é o ID da cidade
        nome = item_values[1]  # O segundo valor é o nome da cidade
        uf = item_values[2]  # O terceiro valor é o UF

        # Abre a janela de edição
        edit_window = CidadesEDITWindow(self.root, cidade_id, nome, uf)
        self.root.wait_window(edit_window.window)  # Aguarda o fechamento da janela antes de atualizar os dados
        self.reload_data()  # Recarrega os dados após editar ou excluir

# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    app = CidadesVIEWWindow(root)
    root.bind("<Double-1>", app.on_item_double_click)  # Liga o evento de duplo clique
    root.mainloop()

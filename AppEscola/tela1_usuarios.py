import tkinter as tk
from tkinter import ttk, messagebox
from crude import select_usuarios, add_usuario, update_usuario, delete_usuario

# Classe da janela de adição de usuários
class UsuariosADDWindow:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Cadastro de Usuários")

        self.entry_nome = tk.Entry(self.window)
        self.entry_username = tk.Entry(self.window)
        self.entry_senha = tk.Entry(self.window, show="*")

        tk.Label(self.window, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.window, text="Username:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.window, text="Senha:").grid(row=2, column=0, padx=10, pady=10)

        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)
        self.entry_senha.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.window, text="Voltar", command=self.window.destroy).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.window, text="Adicionar", command=self.save_data).grid(row=3, column=1, padx=10, pady=10)

    def save_data(self):
        nome = self.entry_nome.get()
        username = self.entry_username.get()
        senha = self.entry_senha.get()
        
        if nome and username and senha:
            add_usuario(nome, username, senha)
            self.window.destroy()
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos")


# Classe da janela de edição de usuários
class UsuariosEDITWindow:
    def __init__(self, master, usuario_id, nome, username, senha):
        self.window = tk.Toplevel(master)
        self.window.title("Editar Usuário")

        self.entry_nome = tk.Entry(self.window)
        self.entry_nome.insert(0, nome)

        self.entry_username = tk.Entry(self.window)
        self.entry_username.insert(0, username)

        self.entry_senha = tk.Entry(self.window, show="*")
        self.entry_senha.insert(0, senha)

        tk.Label(self.window, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.window, text="Username:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.window, text="Senha:").grid(row=2, column=0, padx=10, pady=10)

        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)
        self.entry_senha.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.window, text="Salvar", command=lambda: self.save_changes(usuario_id)).grid(row=3, column=0, padx=5, pady=10)
        tk.Button(self.window, text="Excluir", command=lambda: self.delete_usuario(usuario_id)).grid(row=3, column=1, padx=5, pady=10)

    def save_changes(self, usuario_id):
        nome_novo = self.entry_nome.get()
        username_novo = self.entry_username.get()
        senha_nova = self.entry_senha.get()

        if nome_novo and username_novo and senha_nova:
            update_usuario(usuario_id, nome_novo, username_novo, senha_nova)
            self.window.destroy()
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos corretamente")

    def delete_usuario(self, usuario_id):
        confirm = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir este usuário?")
        if confirm:
            delete_usuario(usuario_id)
            self.window.destroy()


# Classe da janela principal de visualização de usuários
class UsuariosVIEWWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Usuários")

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        self.add_button = tk.Button(main_frame, text="Adicionar Usuário", command=self.open_add_window)
        self.add_button.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(main_frame, columns=("ID", "Nome", "Username"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Username", text="Username")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_data()

        # Campos de pesquisa
        self.create_search_fields(main_frame)

    def create_search_fields(self, frame):
        # Criação de campos de pesquisa dinâmicos com base nas colunas do Treeview
        tk.Label(frame, text="Pesquisar Nome:").pack(side=tk.LEFT)
        self.entry_nome_search = tk.Entry(frame)
        self.entry_nome_search.pack(side=tk.LEFT)
        

        tk.Button(frame, text="Buscar", command=self.search_button_click).pack(side=tk.LEFT)

    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        usuarios = select_usuarios()
        for usuario in usuarios:
            self.tree.insert("", tk.END, values=usuario)

    def open_add_window(self):
        add_window = UsuariosADDWindow(self.root)
        self.root.wait_window(add_window.window)
        self.reload_data()

    def reload_data(self):
        self.load_data()

    def on_item_double_click(self, event):
        item_id = self.tree.selection()[0]
        item_values = self.tree.item(item_id, "values")

        usuario_id = item_values[0]
        nome = item_values[1]
        username = item_values[2]

        edit_window = UsuariosEDITWindow(self.root, usuario_id, nome, username, "")
        self.root.wait_window(edit_window.window)
        self.reload_data()

    def search_button_click(self):
        # Função de busca
        nome = self.entry_nome_search.get().strip()

        # Pega todos os usuários
        usuarios = select_usuarios()

        # Filtrar usuários com base nos critérios de pesquisa
        usuarios_filtrados = [
            usuario for usuario in usuarios
            if not nome or nome.lower() in usuario[1].lower()
        ]

        self.tree.delete(*self.tree.get_children())  # Limpa o Treeview
        for usuario in usuarios_filtrados:
            self.tree.insert("", tk.END, values=usuario)


# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    app = UsuariosVIEWWindow(root)
    root.bind("<Double-1>", app.on_item_double_click)
    root.mainloop()

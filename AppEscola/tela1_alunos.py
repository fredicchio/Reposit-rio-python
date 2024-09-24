import tkinter as tk
from tkinter import ttk
from banco import *

class AlunosWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Alunos")

        # Conectar ao banco de dados
        self.conn, self.cursor = self.connect_db()

        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Botão de Adicionar
        self.add_button = tk.Button(main_frame, text="Adicionar Aluno", command=self.open_add_window)
        self.add_button.pack(side=tk.LEFT)

        # Treeview
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Nome", "Endereço", "Email", "Telefone", "Idade"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Endereço", text="Endereço")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Idade", text="Idade")
        self.tree.bind("<Double-1>", self.on_item_click)
        self.tree.pack(fill=tk.BOTH, expand=1)

        # Campos de pesquisa
        self.create_search_fields(main_frame)

        # Carregar dados iniciais
        self.load_data()

    def load_data(self):
        # Função para carregar os dados do banco no Treeview
        self.cursor.execute("SELECT * FROM tbl_alunos")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def create_search_fields(self, frame):
        # Criação de campos de pesquisa dinâmicos com base nas colunas do Treeview
        columns = ["Nome", "Endereço", "Email", "Telefone", "Idade"]
        for col in columns:
            lbl = tk.Label(frame, text=f"Pesquisar {col}:")
            lbl.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)

    def on_item_click(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, "values")
        self.open_edit_window(values)

    def open_edit_window(self, values):
        # Abre uma nova janela para editar ou excluir o aluno
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar/Excluir Aluno")

        tk.Label(edit_window, text="Nome:").pack()
        nome_entry = tk.Entry(edit_window)
        nome_entry.insert(0, values[1])
        nome_entry.pack()

        # Implementar campos adicionais e botões de salvar e excluir
        tk.Button(edit_window, text="Salvar Alterações", command=lambda: self.save_changes(values[0], nome_entry.get())).pack()
        tk.Button(edit_window, text="Excluir", command=lambda: self.delete_aluno(values[0])).pack()
        tk.Button(edit_window, text="Voltar", command=edit_window.destroy).pack()

    def save_changes(self, aluno_id, nome):
        # Implementar a lógica para salvar as alterações no banco de dados
        query = "UPDATE tbl_alunos SET Nome = %s WHERE Id = %s"
        self.cursor.execute(query, (nome, aluno_id))
        self.conn.commit()
        self.load_data()  # Atualizar o Treeview

    def delete_aluno(self, aluno_id):
        # Implementar a lógica para excluir o aluno do banco de dados
        query = "DELETE FROM tbl_alunos WHERE Id = %s"
        self.cursor.execute(query, (aluno_id,))
        self.conn.commit()
        self.load_data()  # Atualizar o Treeview

    def open_add_window(self):
        # Abre uma nova janela para adicionar um novo aluno
        add_window = tk.Toplevel(self.root)
        add_window.title("Adicionar Aluno")

        tk.Label(add_window, text="Nome:").pack()
        nome_entry = tk.Entry(add_window)
        nome_entry.pack()
        
        tk.Label(add_window, text="Endereco:").pack()
        endereco_entry = tk.Entry(add_window)
        endereco_entry.pack()

        tk.Label(add_window, text="Email:").pack()
        email_entry = tk.Entry(add_window)
        email_entry.pack()

        tk.Label(add_window, text="Telefone:").pack()
        telefone_entry = tk.Entry(add_window)
        telefone_entry.pack()

        tk.Label(add_window, text="Data de nascimento:").pack()
        datanascimento_entry = tk.Entry(add_window)
        datanascimento_entry.pack()



        # Campos adicionais
        tk.Button(add_window, text="Adicionar", command=lambda: self.add_aluno(nome_entry.get(), endereco_entry.get(), email_entry.get(), telefone_entry.get(), datanascimento_entry.get(),)).pack()
        tk.Button(add_window, text="Voltar", command=add_window.destroy).pack()

    def add_aluno(self, nome, endereco, email, telefone, idade):
        # Implementar a lógica para adicionar um novo aluno no banco de dados
        query = "INSERT INTO tbl_alunos (Nome) VALUES (%s,%s,%s,%s,%s)"
        self.cursor.execute(query, (nome,endereco,email,telefone,idade,))
        self.conn.commit()
        self.load_data()  # Atualizar o Treeview

# Inicializar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = AlunosWindow(root)
    root.mainloop()

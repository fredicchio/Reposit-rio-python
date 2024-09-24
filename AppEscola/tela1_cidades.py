import tkinter as Tkinter
from tkinter import ttk
from banco import *

class CidadesWindow:
    def __init__(self, master):
        self.window = Tkinter.Toplevel(master)
        self.window.title("Cadastro de cidades")

        # Criando 3 entradas
        self.entry1 = Tkinter.Entry(self.window)

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
        Tkinter.Label(self.window, text="Cidade:").grid(row=0, column=0, padx=10, pady=10)
        Tkinter.Label(self.window, text="Estado:").grid(row=1, column=0, padx=10, pady=10)

        # Criando 3 botões: Salvar, Limpar, Voltar
        Tkinter.Button(self.window, text="Voltar", command=self.window.destroy).grid(row=2, column=0, padx=10, pady=10)
        Tkinter.Button(self.window, text="Adicionar", command=self.save_data).grid(row=2, column=1, padx=10, pady=10)

    # Função para salvar os dados (lógica a ser implementada)
    def save_data(self):
        try:
            # Exemplo de como capturar os dados inseridos
            campo1 = self.entry1.get()
            estado = self.combobox.get()
            # Aqui você pode adicionar a lógica para salvar os dados no banco
            conn, cursor = cb()

            sql = "INSERT INTO tbl_cidades (nome, UF) VALUES (%s, %s)"
            val = (campo1, estado)

            cursor.execute(sql,val)
            conn.commit()

        except Error as e:
            print(f"Erro ao conectar ao banco de dados : {e}")
        finally:
            fc(conn, cursor)

    # Função para limpar os campos
    def clear_fields(self):
        self.entry1.delete(0, Tkinter.END)
        self.combobox.set("Selecione um Estado")

# Exemplo de uso:
# root = Tkinter.Tk()
# app = CidadesWindow(root)
# root.mainloop()


import tkinter as Tkinter

class AulasWindow:
    def __init__(self, master):
        self.window = Tkinter.Toplevel(master)
        self.window.title("Cadastro de Alunos")

        # Criando 3 entradas
        self.entry1 = Tkinter.Entry(self.window)
        self.entry2 = Tkinter.Entry(self.window)
        self.entry3 = Tkinter.Entry(self.window)

        self.entry1.grid(row=0, column=1, padx=10, pady=10)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)
        self.entry3.grid(row=2, column=1, padx=10, pady=10)

        Tkinter.Label(self.window, text="Campo 1:").grid(row=0, column=0, padx=10, pady=10)
        Tkinter.Label(self.window, text="Campo 2:").grid(row=1, column=0, padx=10, pady=10)
        Tkinter.Label(self.window, text="Campo 3:").grid(row=2, column=0, padx=10, pady=10)

        # Criando 3 botões
        Tkinter.Button(self.window, text="Salvar", command=self.save_data).grid(row=3, column=0, padx=10, pady=10)
        Tkinter.Button(self.window, text="Limpar", command=self.clear_fields).grid(row=3, column=1, padx=10, pady=10)
        Tkinter.Button(self.window, text="Voltar", command=self.window.destroy).grid(row=3, column=2, padx=10, pady=10)

    def save_data(self):
        # Função para salvar dados (implementar conforme necessário)
        print("Dados salvos!")

    def clear_fields(self):
        # Função para limpar os campos de entrada
        self.entry1.delete(0, Tkinter.END)
        self.entry2.delete(0, Tkinter.END)
        self.entry3.delete(0, Tkinter.END)

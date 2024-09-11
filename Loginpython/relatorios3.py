import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from manutencao import busuarios, bcidades, bclientes
import os

caminho_arquivo = ''

class Relatorio:
    def __init__(self, root):
        self.root = root
        self.root.title("Exportar Relatórios para PDF")
        
        # Botão para exportar dados de clientes para PDF
        self.botao_exportar_clientes = tk.Button(root, text="Exportar dados de clientes para PDF", command=self.exportar_clientes_para_pdf)
        self.botao_exportar_clientes.pack()

        # Botão para exportar dados de cidades para PDF
        self.botao_exportar_cidades = tk.Button(root, text="Exportar dados de cidades para PDF", command=self.exportar_cidades_para_pdf)
        self.botao_exportar_cidades.pack()

        # Botão para exportar dados de usuários para PDF
        self.botao_exportar_usuarios = tk.Button(root, text="Exportar dados de usuários para PDF", command=self.exportar_usuarios_para_pdf)
        self.botao_exportar_usuarios.pack()

    def get_search_usuarios(self):
        usuarios_instance = busuarios()
        usuarios = usuarios_instance.selectall()
        return usuarios

    def get_search_cidades(self):
        cidades_instance = bcidades()
        cidades = cidades_instance.selectall()
        return cidades

    def get_search_clientes(self):
        clientes_instance = bclientes()
        clientes = clientes_instance.selectall()
        return clientes

    def exportar_clientes_para_pdf(self):
        clientes = self.get_search_clientes()
        pdf_file = "clientes_exportados.pdf"
        with PdfPages(pdf_file) as pdf:
            fig, axs = plt.subplots(figsize=(8.27, 11.69))  # Tamanho A4
            axs.axis('tight')
            axs.axis('off')
            axs.table(cellText=clientes, colLabels=['ID', 'Nome', 'Telefone', 'Email', 'Cidade'], loc='center')
            axs.set_title('Clientes')
            pdf.savefig()
            plt.close()
        print("PDF de clientes exportado com sucesso.")


        msg = messagebox.askyesno("Relatório","Relatório gerado com sucesso, deseja abrí-lo?")
        if msg:
            os.startfile(pdf_file)



    def exportar_cidades_para_pdf(self):
        cidades = self.get_search_cidades()
        pdf_file = "cidades_exportadas.pdf"
        with PdfPages(pdf_file) as pdf:
            fig, axs = plt.subplots(figsize=(8.27, 11.69))  # Tamanho A4
            axs.axis('tight')
            axs.axis('off')
            axs.table(cellText=cidades, colLabels=['ID', 'Nome', 'UF'], loc='center')
            axs.set_title('Cidades')
            pdf.savefig()
            plt.close()
        print("PDF de cidades exportado com sucesso.")

        msg = messagebox.askyesno("Relatório","Relatório gerado com sucesso, deseja abrí-lo?")
        if msg:
            os.startfile(pdf_file)



    def exportar_usuarios_para_pdf(self):
        usuarios = self.get_search_usuarios()
        pdf_file = "usuarios_exportados.pdf"
        with PdfPages(pdf_file) as pdf:
            fig, axs = plt.subplots(figsize=(8.27, 11.69))  # Tamanho A4
            axs.axis('tight')
            axs.axis('off')
            axs.table(cellText=usuarios, colLabels=['ID', 'Nome', 'Telefone', 'Email', 'Usuário', 'Senha'], loc='center')
            axs.set_title('Usuários')
            pdf.savefig()
            plt.close()
        print("PDF de usuários exportado com sucesso.")

        msg = messagebox.askyesno("Relatório","Relatório gerado com sucesso, deseja abrí-lo?")
        if msg:
            os.startfile(pdf_file)


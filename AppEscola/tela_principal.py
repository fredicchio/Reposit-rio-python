import tkinter as tk
from tela1_alunos import AlunosWindow
from tela1_aulas import AulasWindow
from tela1_cidades import CidadesWindow
from tela1_cursos import CursosWindow
from tela1_materias import MateriasWindow
from tela1_professores import ProfessoresWindow
from tela1_usuarios import UsuariosWindow

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")

        # Criando o menu
        menubar = Tkinter.Menu(self.root, relief=Tkinter.FLAT)
        self.root.config(menu=menubar)

        filemenu = Tkinter.Menu(menubar, tearoff=0, relief=Tkinter.FLAT)
        menubar.add_cascade(label="Arquivo", menu=filemenu)
        filemenu.add_command(label="Sair", command=self.root.quit)

        cadastro_menu = Tkinter.Menu(menubar, tearoff=0, relief=Tkinter.FLAT)
        menubar.add_cascade(label="Cadastros", menu=cadastro_menu)
        cadastro_menu.add_command(label="Alunos", command=self.open_alunos)
        cadastro_menu.add_command(label="Aulas", command=self.open_aulas)
        cadastro_menu.add_command(label="Cidades", command=self.open_cidades)
        cadastro_menu.add_command(label="Cursos", command=self.open_cursos)
        cadastro_menu.add_command(label="Matérias", command=self.open_materias)
        cadastro_menu.add_command(label="Professores", command=self.open_professores)
        cadastro_menu.add_command(label="Usuários", command=self.open_usuarios)

    def open_alunos(self):
        AlunosWindow(self.root)

    def open_aulas(self):
        AulasWindow(self.root)

    def open_cidades(self):
        CidadesWindow(self.root)

    def open_cursos(self):
        CursosWindow(self.root)

    def open_materias(self):
        MateriasWindow(self.root)

    def open_professores(self):
        ProfessoresWindow(self.root)

    def open_usuarios(self):
        UsuariosWindow(self.root)

    def abrir_tela_principal(self):
        # Fecha a tela de login e abre a tela principal
        self.destroy()
        root = tk.Tk()
        MainApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tkinter.Tk()
    app = MainApp(root)
    root.mainloop()

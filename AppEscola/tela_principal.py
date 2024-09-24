import tkinter as tk
from tela1_alunos import AlunosWindow
from tela1_aulas import AulasWindow
from tela2_cidades import CidadesVIEWWindow
from tela1_cursos import CursosWindow
from tela1_materias import MateriasWindow
from tela1_professores import ProfessoresWindow
from tela1_usuarios import UsuariosVIEWWindow

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")

        # Variável para armazenar a janela atual
        self.current_window = None

        # Criando o menu
        menubar = tk.Menu(self.root, relief=tk.FLAT)
        self.root.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0, relief=tk.FLAT)
        menubar.add_cascade(label="Arquivo", menu=filemenu)
        filemenu.add_command(label="Sair", command=root.destroy)

        cadastro_menu = tk.Menu(menubar, tearoff=0, relief=tk.FLAT)
        menubar.add_cascade(label="Cadastros", menu=cadastro_menu)
        cadastro_menu.add_command(label="Alunos", command=self.open_alunos)
        cadastro_menu.add_command(label="Aulas", command=self.open_aulas)
        cadastro_menu.add_command(label="Cidades", command=self.open_cidades)
        cadastro_menu.add_command(label="Cursos", command=self.open_cursos)
        cadastro_menu.add_command(label="Matérias", command=self.open_materias)
        cadastro_menu.add_command(label="Professores", command=self.open_professores)
        cadastro_menu.add_command(label="Usuários", command=self.open_usuarios)

    def open_alunos(self):
        self.switch_window(AlunosWindow)

    def open_aulas(self):
        self.switch_window(AulasWindow)

    def open_cidades(self):
        self.switch_window(CidadesVIEWWindow)

    def open_cursos(self):
        self.switch_window(CursosWindow)

    def open_materias(self):
        self.switch_window(MateriasWindow)

    def open_professores(self):
        self.switch_window(ProfessoresWindow)

    def open_usuarios(self):
        self.switch_window(UsuariosVIEWWindow)

    def switch_window(self, window_class):
        """Fecha a janela atual, se houver, e abre uma nova."""
        if self.current_window is not None:
            self.current_window.destroy()  # Fecha a janela anterior

        # Cria a nova janela como uma instância de Toplevel
        self.current_window = tk.Toplevel(self.root)
        window_class(self.current_window)  # Passa o Toplevel para a nova janela

    def abrir_tela_principal(self):
        # Fecha a tela de login e abre a tela principal
        self.destroy()
        root = tk.Tk()
        MainApp(root)
        root.mainloop()

root = tk.Tk()
app = MainApp(root)
root.mainloop()

import tkinter as tk
from tkinter import Canvas
from conecta import *


class DesenhoTela(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Desenho da Tela")

        # Obter resolução da tela
        screen_width, screen_height = self.get_screen_resolution()
        self.geometry(f"{screen_width}x{screen_height}")

        # Cores
        gray = "#A9A9A9"
        white_color = "#FFFFFF"
        red_border_color = "#FF0000"

        # Canvas
        self.canvas = Canvas(self, width=screen_width, height=screen_height)
        self.canvas.pack()

        # Multiplicador de tamanho
        if screen_width > screen_height:
            scale_factor = screen_width / screen_height * 2.8125
        else:
            scale_factor = screen_height / screen_width * 2.8125

        # Altura da faixa superior cinza
        header_height = 50 * scale_factor

        # Faixa superior cinza
        self.canvas.create_rectangle(0, 0, screen_width, header_height, fill=gray, outline=gray)

        # Quadrado e retângulo branco na faixa cinza
        self.canvas.create_rectangle(10 * scale_factor, 10 * scale_factor, 30 * scale_factor, 30 * scale_factor, fill=white_color)
        self.canvas.create_text(20 * scale_factor, 20 * scale_factor, text="1", font=("Arial", 12))

        self.canvas.create_rectangle(40 * scale_factor, 10 * scale_factor, 140 * scale_factor, 30 * scale_factor, fill=white_color)
        self.canvas.create_text(90 * scale_factor, 20 * scale_factor, text="2", font=("Arial", 12))

        # Três quadrados brancos com borda vermelha à direita na faixa cinza
        square_size = 20 * scale_factor
        spacing = 10 * scale_factor

        # Primeiro quadrado
        x0 = screen_width - (square_size + spacing) * 3
        y0 = 10 * scale_factor
        x1 = x0 + square_size
        y1 = y0 + square_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=white_color, outline=red_border_color, width=2)
        self.canvas.create_text(x0 + square_size // 2, y0 + square_size // 2, text=str(0 + 3), font=("Arial", 12))

        # Segundo quadrado
        x10 = screen_width - (square_size + spacing) * 2
        y10 = 10 * scale_factor
        x11 = x10 + square_size
        y11 = y10 + square_size
        self.canvas.create_rectangle(x10, y10, x11, y11, fill=white_color, outline=red_border_color, width=2)
        self.canvas.create_text(x10 + square_size // 2, y10 + square_size // 2, text=str(1 + 3), font=("Arial", 12))

        # Terceiro quadrado
        x20 = screen_width - (square_size + spacing)
        y20 = 10 * scale_factor
        x21 = x20 + square_size
        y21 = y20 + square_size
        self.canvas.create_rectangle(x20, y20, x21, y21, fill=white_color, outline=red_border_color, width=2)
        self.canvas.create_text(x20 + square_size // 2, y20 + square_size // 2, text=str(2 + 3), font=("Arial", 12))

        # Retângulo branco principal
        self.canvas.create_rectangle(0, header_height, screen_width, screen_height, fill=white_color, outline=white_color)

        # Lateral vermelha com quadrados brancos
        side_bar_width = 25 * scale_factor + header_height
        self.canvas.create_rectangle(0, header_height, side_bar_width, screen_height, fill=red_border_color, outline=red_border_color)

        # Funções para abrir novas janelas
        button_functions = [self.open_recursos, self.open_agenda, self.open_materiais, self.open_relatorios]
        button_labels = ["Recursos", "Agenda", "Materiais", "Relatórios"]

        easy = int(scale_factor)
        for i in range(4):
            button = tk.Button(self, text=str(i + 6), command=button_functions[i], width=2 * easy, height=easy)
            button.place(x=side_bar_width / 3, y=(header_height + screen_height / 20) + (i * (side_bar_width / 3 + screen_height / 20)))

        # Coordenadas dos vértices do quadrado vermelho (botões 3, 4, 5)
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.x10, self.y10, self.x11, self.y11 = x10, y10, x11, y11
        self.x20, self.y20, self.x21, self.y21 = x20, y20, x21, y21

        # Variáveis para armazenar as coordenadas do clique do mouse e status do quadrado azul e verde
        self.x, self.y = 0, 0
        self.a = 0  # Inicializa 'a' fora da função para ser global
        self.blue_square = None
        self.label = None
        self.button = None
        self.green_block = None
        self.purple_block = None

        # Vincula o evento de clique do mouse ao canvas
        self.canvas.bind("<Button-1>", self.on_click)

    def get_screen_resolution(self):
        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return width, height

    def open_recursos(self):
        from materiais import CadastroMateriais

        conn, cursor = conectar_ao_banco() 
        CadastroMateriais(self.master, conn, cursor)

    def open_agenda(self):
        from frames_reservas import CalendarApp

        conn, cursor = conectar_ao_banco() 
        CalendarApp(self.master, conn, cursor)


    def open_materiais(self):
        new_window = tk.Toplevel(self)
        new_window.title("Materiais")
        new_window.geometry("600x400")
        tk.Label(new_window, text="Materiais").pack()
        tk.Button(new_window, text="Voltar", command=new_window.destroy).pack()

    def open_relatorios(self):
        new_window = tk.Toplevel(self)
        new_window.title("Relatórios")
        new_window.geometry("600x400")
        tk.Label(new_window, text="Relatórios").pack()
        tk.Button(new_window, text="Voltar", command=new_window.destroy).pack()

    def on_click(self, event):
        self.x, self.y = event.x, event.y
        print(f"Posição do clique: x={self.x}, y={self.y}")
        
        # Verifica se o clique está dentro da área do quadrado 3
        if self.a == 0 and (self.x0 <= self.x <= self.x1) and (self.y0 <= self.y <= self.y1):
            print("dentro do 3")
            if self.blue_square is None:
                self.blue_square = self.canvas.create_rectangle(self.winfo_screenwidth() // 3, self.winfo_screenheight() // 3, self.winfo_screenwidth() // 3 * 2, self.winfo_screenheight() // 3 * 2, fill="blue")
                self.label = tk.Label(self, text="Quadrado Azul", bg="blue", fg="white")
                self.label.place(x=self.winfo_screenwidth() // 3, y=self.winfo_screenheight() // 3 - 30)
                self.button = tk.Button(self, text="Clique Aqui", command=self.destroy_blue_square)
                self.button.place(x=self.winfo_screenwidth() // 3 + 10, y=self.winfo_screenheight() // 3 + 10)
                self.a = 1  # Define 'a' como 1 quando o quadrado azul é criado

        # Verifica se o clique está dentro da área do quadrado 4
        elif self.a == 0 and (self.x10 <= self.x <= self.x11) and (self.y10 <= self.y <= self.y11):
            print("dentro do 4")
            if self.green_block is None:
                self.green_block = self.canvas.create_rectangle(self.winfo_screenwidth() // 3, self.winfo_screenheight() // 3, self.winfo_screenwidth() // 3 * 2, self.winfo_screenheight() // 3 * 2, fill="green")
                self.a = 2  # Define 'a' como 2 quando o bloco verde é criado

        # Verifica se o clique está dentro da área do quadrado 5
        elif self.a == 0 and (self.x20 <= self.x <= self.x21) and (self.y20 <= self.y <= self.y21):
            print("dentro do 5")
            if self.purple_block is None:
                self.purple_block = self.canvas.create_rectangle(self.winfo_screenwidth() // 3, self.winfo_screenheight() // 3, self.winfo_screenwidth() // 3 * 2, self.winfo_screenheight() // 3 * 2, fill="purple")
                self.a = 3

        else:
            self.a = 0

        if self.a == 0 and not ((self.winfo_screenwidth() // 3 <= self.x <= self.winfo_screenwidth() // 3 * 2) and (self.winfo_screenheight() // 3 <= self.y <= self.winfo_screenheight() // 3 * 2)):
            self.destroy_blue_square()
            self.destroy_green_block()
            self.destroy_purple_block()

        print(self.a)

    def destroy_blue_square(self):
        if self.blue_square is not None:
            self.canvas.delete(self.blue_square)
            self.blue_square = None
        if self.label is not None:
            self.label.destroy()
            self.label = None
        if self.button is not None:
            self.button.destroy()
            self.button = None
        self.a = 0

    def destroy_green_block(self):
        if self.green_block is not None:
            self.canvas.delete(self.green_block)
            self.green_block = None
        self.a = 0

    def destroy_purple_block(self):
        if self.purple_block is not None:
            self.canvas.delete(self.purple_block)
            self.purple_block = None
        self.a = 0

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    app = DesenhoTela(root)
    app.mainloop()
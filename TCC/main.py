from tkinter import *
import customtkinter as ctk
from conecta import conectar_ao_banco
from auth_login import Login

class MainApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x800")
        self.db, _ = conectar_ao_banco()
        self._frame = None
        self.switch_frame(Login)

    def switch_frame(self, frame_class):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame_class(self)
        self._frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Tema escuro
    ctk.set_default_color_theme("green")  # Tema de cor verde
    app = MainApp()
    app.mainloop()

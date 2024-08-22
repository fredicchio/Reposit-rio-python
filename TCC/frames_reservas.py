import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import calendar
from conecta import *
from frames_main_frame import DesenhoTela


class CalendarApp:
    def __init__(self, root, conn, cursor):
        self.root = root
        self.root.title("Calendário")

        self.selected_date = None
        self.conn = conn
        self.cursor = cursor

        self.create_widgets()
        self.show_calendar(datetime.now().year, datetime.now().month)

        # Lista de opções para o OptionMenu
        self.opcoes = ["Sala 1", "Sala 2", "Sala 3", "Sala 4"]

        # Variável para armazenar a opção selecionada
        self.opcao_var = tk.StringVar(self.root)
        self.opcao_var.set(self.opcoes[0])  # Define a primeira opção como padrão

        # Criando o OptionMenu
        opcao_menu = tk.OptionMenu(self.root, self.opcao_var, *self.opcoes)
        opcao_menu.grid(row=0, column=5, padx=20, pady=20)

        self.voltar_button = tk.Button(self.root, text="Voltar", command=self.voltar)
        self.voltar_button.grid(row=0, column=8, padx=10)

        self.desmarcar_button = tk.Button(self.root, text="Desmarcar", command=self.open_desmarcar)
        self.desmarcar_button.grid(row=0, column=6)

        self.ver_reservas_button = tk.Button(self.root, text="Ver Reservas", command=self.ver_reservas)
        self.ver_reservas_button.grid(row=0, column=7)

    def create_widgets(self):
        # Criação de entradas e rótulos para ano e mês
        self.year_label = tk.Label(self.root, text="Ano:")
        self.year_label.grid(row=0, column=0)
        self.year_var = tk.StringVar(value=str(datetime.now().year))
        self.year_entry = tk.Entry(self.root, textvariable=self.year_var)
        self.year_entry.grid(row=0, column=1)

        self.month_label = tk.Label(self.root, text="Mês:")
        self.month_label.grid(row=0, column=2)
        self.month_var = tk.StringVar(value=str(datetime.now().month))
        self.month_entry = tk.Entry(self.root, textvariable=self.month_var)
        self.month_entry.grid(row=0, column=3)

        # Botão para mostrar o calendário
        self.show_button = tk.Button(self.root, text="Mostrar Calendário", command=self.update_calendar)
        self.show_button.grid(row=0, column=4)

        self.cal_frame = tk.Frame(self.root)
        self.cal_frame.grid(row=1, column=0, columnspan=8)

    def show_calendar(self, year, month):
        for widget in self.cal_frame.winfo_children():
            widget.destroy()

        cal = calendar.monthcalendar(year, month)
        days = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']

        for col, day in enumerate(days):
            tk.Label(self.cal_frame, text=day).grid(row=0, column=col)

        for row, week in enumerate(cal, start=1):
            for col, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.cal_frame, text=str(day), command=lambda d=day: self.select_date(year, month, d))
                    btn.grid(row=row, column=col)

    def update_calendar(self):
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            self.show_calendar(year, month)
        except ValueError:
            messagebox.showerror("Erro de entrada", "Ano e mês devem ser números inteiros válidos.")

    def select_date(self, year, month, day):
        self.selected_date = datetime(year, month, day)
        selected_room = self.opcao_var.get()
        print(f"Data selecionada: {self.selected_date}, Sala selecionada: {selected_room}")
        self.open_horarios_do_dia()

    def open_horarios_do_dia(self):
        HorariosDoDia(self.root, self.conn, self.cursor, self.marcar_horarios, self.selected_date, self.opcao_var.get())

    def marcar_horarios(self, horarios_selecionados):
        print(f"Horários marcados: {horarios_selecionados}")
        # Aqui você pode adicionar a lógica para salvar os horários selecionados no banco de dados.

    def voltar(self):
        # Feche a janela atual e reabra a tela de desenho
        self.root.destroy()
        new_root = tk.Tk()
        DesenhoTela(new_root)
        new_root.mainloop()
        
    def open_desmarcar(self):
        DesmarcarHorarios(self.root, self.conn, self.cursor, self.selected_date, self.opcao_var.get())

    def ver_reservas(self):
        VerReservas(self.root, self.conn, self.cursor, self.opcao_var.get())

class HorariosDoDia:
    def __init__(self, master, conn, cursor, callback, data, selected_room):
        self.root = tk.Toplevel(master)
        self.root.title(f"Horários do Dia - {data.strftime('%d/%m/%Y')} - {selected_room}")
        self.selected_room = selected_room

        # Obter o nome do usuário atual armazenado no master
        self.master = master  # Guardar a referência ao master
        global usuario
        usuario = self.master.current_user  # Acessar o current_user do master
        print(usuario)

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.master = master
        self.data_selecionada = data
        self.horarios_selecionados = []

        self.horarios_disponiveis = [
            7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
        ]

        self.botoes_horarios = []

        # Buscar horários reservados e armazenar em reservas
        self.horarios_reservados = self.buscar_horarios_reservados(conn, cursor, self.data_selecionada, self.selected_room)
        print(self.horarios_reservados)

        # Criar botões de horários
        for horario in self.horarios_disponiveis:
            cor_fundo = "white"
            estado = "normal"
            if horario in self.horarios_reservados:
                cor_fundo = "red"
                estado = "disabled"  # Desativar o botão
            botao = tk.Button(self.frame, text=horario, width=10, bg=cor_fundo, state=estado, command=lambda h=horario: self.toggle_selecao(h))
            botao.pack(pady=5)
            self.botoes_horarios.append(botao)

        self.marcar_button = tk.Button(self.frame, text="Marcar", command=self.marcar_horarios)
        self.marcar_button.pack(pady=10)

        self.conn = conn
        self.cursor = cursor
        self.callback = callback

    def toggle_selecao(self, horario):
        if horario in self.horarios_selecionados:
            self.horarios_selecionados.remove(horario)
            self.atualizar_cor(horario, "white")
        else:
            self.horarios_selecionados.append(horario)
            self.atualizar_cor(horario, "yellow")

    def marcar_horarios(self):
        if self.horarios_selecionados:
            self.horarios_selecionados.sort()
            
            primeiro_horario = self.horarios_selecionados[0] * 10000
            ultimo_horario = self.horarios_selecionados[-1] * 10000 + 10000

            try:
                # Executar o SELECT no banco de dados para obter os detalhes do usuário
                self.cursor.execute("SELECT usu_nome FROM usuario WHERE usu_usuario = %s", (usuario,))
                
                # Ler todos os resultados da consulta
                resultados = self.cursor.fetchall()

                # Verificar se há resultados
                if resultados:
                    nome = resultados[0][0]  # Extraindo o nome do primeiro usuário encontrado
                    self.inserir_reserva(self.conn, self.cursor, self.selected_room, nome, primeiro_horario, ultimo_horario, self.data_selecionada.strftime('%Y-%m-%d'))
                else:
                    print(f"Usuário {usuario} não encontrado no banco de dados.")

            except Error as e:
                print(f"Erro ao executar consulta SQL: {e}")

        self.callback(self.horarios_selecionados)
        self.root.destroy()

    def atualizar_cor(self, horario, cor):
        for botao in self.botoes_horarios:
            if botao.cget("text") == horario:
                botao.config(bg=cor)

    def buscar_horarios_reservados(self, conn, cursor, data, selected_room):
        try:
            cursor.execute("""
                SELECT HOUR(primeiro_horario), HOUR(ultimo_horario) FROM reservas
                WHERE data_reserva = %s AND laboratorio = %s
            """, (data.strftime('%Y-%m-%d'), selected_room))
            resultados = cursor.fetchall()
            
            horarios_reservados = []
            for primeiro, ultimo in resultados:
                horarios_reservados.extend(range(primeiro, ultimo + 1))
            
            return horarios_reservados
        except Error as e:
            print(f"Erro ao buscar horários reservados: {e}")
            return []

    def inserir_reserva(self, conn, cursor, laboratorio, pessoa, primeiro_horario, ultimo_horario, data_reserva):
        try:
            cursor.execute("""
                INSERT INTO reservas (laboratorio, pessoa, primeiro_horario, ultimo_horario, data_reserva)
                VALUES (%s, %s, %s, %s, %s)
            """, (laboratorio, pessoa, primeiro_horario, ultimo_horario, data_reserva))
            conn.commit()
        except Error as e:
            print(f"Erro ao inserir a reserva: {e}")

class DesmarcarHorarios:
    def __init__(self, master, conn, cursor, data, selected_room):
        self.root = tk.Toplevel(master)
        self.root.title(f"Desmarcar Horários - {data.strftime('%d/%m/%Y')} - {selected_room}")
        self.selected_room = selected_room

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.master = master
        self.data_selecionada = data
        self.horarios_selecionados = []

        self.horarios_disponiveis = [
            7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
        ]

        self.botoes_horarios = []

        # Buscar horários reservados e armazenar em reservas
        self.horarios_reservados = self.buscar_horarios_reservados(conn, cursor, self.data_selecionada, self.selected_room)
        print(self.horarios_reservados)

        # Criar botões de horários
        for horario in self.horarios_disponiveis:
            cor_fundo = "white"
            estado = "normal"
            if horario in self.horarios_reservados:
                cor_fundo = "red"
                estado = "normal"  # Ativar o botão se for desmarcar
            botao = tk.Button(self.frame, text=horario, width=10, bg=cor_fundo, state=estado, command=lambda h=horario: self.toggle_selecao(h))
            botao.pack(pady=5)
            self.botoes_horarios.append(botao)

        self.desmarcar_button = tk.Button(self.frame, text="Desmarcar", command=self.desmarcar_horarios)
        self.desmarcar_button.pack(pady=10)

        self.conn = conn
        self.cursor = cursor

    def toggle_selecao(self, horario):
        if horario in self.horarios_selecionados:
            self.horarios_selecionados.remove(horario)
            self.atualizar_cor(horario, "white")
        else:
            self.horarios_selecionados.append(horario)
            self.atualizar_cor(horario, "yellow")

    def desmarcar_horarios(self):
        if self.horarios_selecionados:
            self.horarios_selecionados.sort()

            for horario in self.horarios_selecionados:
                try:
                    # Consulta para verificar se há uma reserva no horário
                    self.cursor.execute("""
                        SELECT pessoa FROM reservas WHERE laboratorio = %s AND data_reserva = %s AND %s BETWEEN HOUR(primeiro_horario) AND HOUR(ultimo_horario)
                    """, (self.selected_room, self.data_selecionada.strftime('%Y-%m-%d'), horario))
                    resultado = self.cursor.fetchone()

                    # Certifique-se de que não há resultados pendentes
                    self.cursor.fetchone()

                    if resultado is None:
                        print(f"Nenhuma reserva encontrada para o horário {horario}:00.")
                        continue

                    # Consulta para obter o nome do usuário com base no identificador
                    self.cursor.execute("""
                        SELECT usu_nome FROM usuario WHERE usu_usuario = %s
                    """, (usuario,))
                    Nome = self.cursor.fetchall()  

                    if Nome is None:
                        print(f"Usuário não encontrado.")
                        continue

                    # Verificar se a pessoa da reserva é a mesma que o usuário
                    if resultado == Nome[0]:
                        self.remover_reserva(self.conn, self.cursor, self.selected_room, horario, self.data_selecionada.strftime('%Y-%m-%d'))
                    else:
                        print(f"Você não tem permissão para desmarcar o horário {horario}:00.")

                except Error as e:
                    print(f"Erro ao verificar ou desmarcar reserva: {e}")

        self.root.destroy()


    def atualizar_cor(self, horario, cor):
        for botao in self.botoes_horarios:
            if botao.cget("text") == horario:
                botao.config(bg=cor)

    def buscar_horarios_reservados(self, conn, cursor, data, selected_room):
        try:
            cursor.execute("""
                SELECT HOUR(primeiro_horario), HOUR(ultimo_horario) FROM reservas
                WHERE data_reserva = %s AND laboratorio = %s
            """, (data.strftime('%Y-%m-%d'), selected_room))
            resultados = cursor.fetchall()

            horarios_reservados = []
            for primeiro, ultimo in resultados:
                horarios_reservados.extend(range(primeiro, ultimo + 1))

            return horarios_reservados
        except Error as e:
            print(f"Erro ao buscar horários reservados: {e}")
            return []

    def remover_reserva(self, conn, cursor, laboratorio, horario, data_reserva):
        try:
            # Comando SQL para remover a reserva
            cursor.execute("""
                DELETE FROM reservas
                WHERE laboratorio = %s AND data_reserva = %s AND %s BETWEEN HOUR(primeiro_horario) AND HOUR(ultimo_horario)
            """, (laboratorio, data_reserva, horario))

            print(laboratorio, data_reserva, horario)
            
            # Confirmar a transação
            conn.commit()
            print(f"Reserva para o horário {horario}:00 removida com sucesso.")
        
        except Error as e:
            print(f"Erro ao remover a reserva: {e}")
            conn.rollback()  # Reverter a transação em caso de erro

class VerReservas:
    def __init__(self, master, conn, cursor, selected_room):
        self.root = tk.Toplevel(master)
        self.root.title(f"Reservas - {selected_room}")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.selected_room = selected_room

        try:
            cursor.execute("""
                SELECT pessoa, data_reserva, HOUR(primeiro_horario), HOUR(ultimo_horario), laboratorio FROM reservas
                WHERE laboratorio = %s
                ORDER BY data_reserva, primeiro_horario
            """, (selected_room,))
            reservas = cursor.fetchall()

            self.tree = ttk.Treeview(self.frame, columns=("Pessoa", "Data", "Início", "Término", "Local"), show="headings")
            self.tree.heading("Pessoa", text="Pessoa")
            self.tree.heading("Data", text="Data")
            self.tree.heading("Início", text="Início")
            self.tree.heading("Término", text="Término")
            self.tree.heading("Local", text="Local")
            self.tree.pack(fill=tk.BOTH, expand=True)

            for reserva in reservas:
                pessoa, data, primeiro_horario, ultimo_horario, local = reserva
                self.tree.insert("", "end", values=(pessoa, data, f"{primeiro_horario}:00", f"{ultimo_horario}:00", local))

        except Error as e:
            print(f"Erro ao buscar reservas: {e}")

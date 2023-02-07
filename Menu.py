import tkinter as tk
import os
from persistencia.bd import BancoDados
from visao.ClienteView import CadastroClientes
from modelo.cadastroIncidente import Inci
from visao.HistoricoIncidentesView import *
from visao.AtendenteView import *

class Menu:
    def __init__(self, window):
        self.window = window

        menuBar = tk.Menu(window)

        cadastroMenu = tk.Menu(menuBar, tearoff=False)
        cadastroMenu.add_command(label="Cadastro de Cliente", command=self._open_cliente)
        cadastroMenu.add_command(label="Cadastro de Atendente", command=self._open_atendente)
        menuBar.add_cascade(menu=cadastroMenu, label="Cadastros")

        registroMenu= tk.Menu(menuBar, tearoff=False)
        registroMenu.add_command(label="Registro de Incidentes", command=self._open_incidente)
        menuBar.add_cascade(menu=registroMenu, label="Incidentes")

        menuConsulta = tk.Menu(menuBar, tearoff=False)
        menuConsulta.add_command(label="Histórico de Incidentes", command=self._open_consulta)
        menuBar.add_cascade(menu=menuConsulta, label="Consulta")

        window.config(menu=menuBar)

    def _open_cliente(self):
        janela = tk.Toplevel(self.window)
        janela.title('Cadastro de Cliente')
        janela.geometry("650x270")
        janela.resizable(width=0, height=0)
        principal = CadastroClientes(janela)
        janela.mainloop()

    def _open_atendente(self):
        janela = tk.Toplevel(self.window)
        janela.title('Cadastro de Atendente')
        janela.geometry("780x300")
        janela.resizable(width=0, height=0)

        principal = CadastroAtendentes(janela)
        janela.mainloop()

    def _open_incidente(self):
        janela = tk.Toplevel(self.window)
        janela.title('Registro de Incidentes')
        janela.geometry("650x270")
        janela.resizable(width=0, height=0)

        principal = Inci(janela)
        janela.mainloop()

    def _open_consulta(self):
        janela = tk.Toplevel(self.window)
        janela.title('Histórico de Incidentes')
        janela.geometry("900x300")
        janela.resizable(width=0, height=0)

        principal = HistoricoIncidentesView(janela)
        janela.mainloop()


import tkinter as tk
from modelo.HistoricoIncidentes import *
from tkinter import ttk
from persistencia.DAOIncidenteP import *
from modelo.HistoricoIncidentes import HistoricoIncidentes
from tkinter import messagebox as mb

class HistoricoIncidentesView:
    def __init__(self, win):
        ##Criação do label e entrada do campo Código
        self.label_codigo = tk.Label(win, text='Código: ')
        self.label_codigo.grid(row=1, column=0, padx=0, pady=10, sticky='nwse', columnspan=1)
        self.entry_codigo = tk.Entry(win, bg="yellow")
        self.entry_codigo.grid(row=1, column=1, padx=0, pady=10, sticky='nswe', columnspan=8)

        ##Criação do label e entrada do campo CPF
        self.label_CPF = tk.Label(win, text='CPF: ')
        self.label_CPF.grid(row=1, column=20, padx=0, pady=10, sticky='nwse', columnspan=8)

        self.entry_CPF = tk.Entry(win, bg="yellow")
        self.entry_CPF.grid(row=1, column=50, padx=0, pady=10, sticky='nswe', columnspan=8)

        ##Criação do botão buscar
        self.btn_buscar = tk.Button(win, text='Buscar', bd=2, command=self.pesquisar)
        self.btn_buscar.grid(row=2, column=80, padx=0, pady=10, sticky='nswe', columnspan=1)

        ##Criação do botão excluir
        self.btn_excluir = tk.Button(win, text='Excluir', bd=2, command=self.on_deletar_clicked)
        self.btn_excluir.grid(row=1,column=80,padx=0,pady=10,sticky='nswe',columnspan=1)

        self.clienteList = ttk.Treeview(win, columns=("COD", "DT", "NOME", "PRIORI", "INCID"), show='headings')
        self.clienteList.heading("#0", text="")
        self.clienteList.heading("COD", text="Código")
        self.clienteList.heading("DT", text="Data")
        self.clienteList.heading("NOME", text="CPF")
        self.clienteList.heading("PRIORI", text="Prioridade")
        self.clienteList.heading("INCID", text="Incidente")

        self.clienteList.column("#0", minwidth=0, width=1)
        self.clienteList.column("COD", minwidth=0, width=50)
        self.clienteList.column("DT", minwidth=0, width=80)
        self.clienteList.column("NOME", minwidth=0, width=120)
        self.clienteList.column("PRIORI", minwidth=0, width=120)
        self.clienteList.column("INCID", minwidth=0, width=120)

        self.clienteList.place(relx=0.02, rely=0.3, relwidth=0.95, relheight=0.6)

    def pesquisar(self):
        self.contacts = []
        try:
            for selected_item in self.clienteList.get_children():
                print(selected_item)
                print(self.clienteList.delete(selected_item))
        except:
            pass

        try:
            self.listaDados = DAOIncidentes.lendobdEsp(self='self', tabela='Incidente', col='idk',
                                                       dados=f'{self.entry_codigo.get()}')  # de acordo com codigo
        except:
            try:
                self.listaDados = DAOIncidentes.lendobdEsp(self='self', tabela='Incidente', col='cpf',
                                                           dados=f'{self.entry_CPF.get()}')  # de acordo com CPF
            except:
                self.listaDados = DAOIncidentes.lendobd(self='self', tabela='Incidente')

        for n in self.listaDados:
            self.contacts.append((f'{n[0]}', f'{n[3]}', f'{n[2]}', f'{n[1]}', f'{n[4]}'))

        # add data to the treeview
        for contact in self.contacts:
            self.clienteList.insert('', tk.END, values=contact)
        # self.contacts.clear()

    def on_deletar_clicked(self):
        linhaSelecionada = self.clienteList.selection()
        self.id_incidente = self.clienteList.item(linhaSelecionada[0])["values"][0]
        try:
            for selected_item in self.clienteList.get_children():
                DAOIncidentes.excluindoInfodb(self='self', tabela='Incidente',coluna='idk',valor=f'{self.id_incidente}')
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.pesquisar()
        except:pass



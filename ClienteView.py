import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from persistencia.DAOClienteV import *

# self.janela = tk.Tk()
#
# janela.title('Cadastro de Clientes')  # Titulo da Janela


class CadastroClientes:

    def __init__(self, win):

        self.lista_estados = ('ACRE-AC', 'ALAGOAS-AL', 'AMAPÁ-AP', 'AMAZONAS-AM', 'BAHIA-BA',
                              'CEARÁ-CE', 'BRASILIA-DF', 'ESPÍRITO SANTO-ES', 'GOIÁS-GO', 'MARANHÃO-MA',
                              'MATO GROSSO-MT', 'MATO GROSSO DO SUL-MS', 'MINAS GERAIS-MG', 'PARÁ-PA',
                              'PARAÍBA-PB', 'PARANÁ-PR', 'PERNAMBUCO-PE', 'PIAUÍ-PI', 'RIO DE JANEIRO-RJ'
                              'RIO GRANDE DO NORTE-RN', 'RIO GRANDE DO SUL-RS', 'RONDÔNIA-RO', 'RORAIMA-RR',
                              'SANTA CATARINA-SC', 'SÃO PAULO-SP', 'SERGIPE-SE', 'TOCANTINS-TO')

        # Labels

        self.label_nomedocliente = tk.Label(win,text='Nome Completo: ')
        self.label_nomedocliente.grid(row=1, column=0, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_cpf = tk.Label(win,text='CPF:')
        self.label_cpf.grid(row=2, column=0, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_telefone = tk.Label(win,text='Telefone: ')
        self.label_telefone.grid(row=2, column=3, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_logradouro = tk.Label(win,text='Logradouro: ')
        self.label_logradouro.grid(row=4, column=0, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_numero = tk.Label(win,text='Número: ')
        self.label_numero.grid(row=5, column=0, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_complemento = tk.Label(win,text='Complemento: ')
        self.label_complemento.grid(row=5, column=3, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_bairro = tk.Label(win,text='Bairro: ')
        self.label_bairro.grid(row=6, column=0, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_cidade = tk.Label(win,text='Cidade: ')
        self.label_cidade.grid(row=6, column=3, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.label_estado = tk.Label(win,text='Estado: ')
        self.label_estado.grid(row=6, column=6, padx=0, pady=10, sticky='nswe', columnspan=1)

        # Entrys

        self.entry_nomedocliente = tk.Entry(win)
        self.entry_nomedocliente.grid(row=1, column=1, padx=0, pady=10, sticky='nswe', columnspan=8)

        self.entry_cpf = tk.Entry(win)
        self.entry_cpf.grid(row=2, column=1, padx=0, pady=10, sticky='nswe', columnspan=2)

        self.entry_telefone = tk.Entry(win)
        self.entry_telefone.grid(row=2, column=4, padx=0, pady=10, sticky='nswe', columnspan=5)

        self.entry_logradouro = tk.Entry(win)
        self.entry_logradouro.grid(row=4, column=1, padx=0, pady=10, sticky='nswe', columnspan=8)

        self.entry_numero = tk.Entry(win)
        self.entry_numero.grid(row=5, column=1, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.entry_complemento = tk.Entry(win)
        self.entry_complemento.grid(row=5, column=4, padx=0, pady=10, sticky='nswe', columnspan=4)

        self.entry_bairro = tk.Entry(win)
        self.entry_bairro.grid(row=6, column=1, padx=0, pady=10, sticky='nswe', columnspan=2)

        self.entry_cidade = tk.Entry(win)
        self.entry_cidade.grid(row=6, column=4, padx=0, pady=10, sticky='nswe', columnspan=1)

        self.combobox_selecionar_estado = ttk.Combobox(win,values=self.lista_estados)
        self.combobox_selecionar_estado.grid(row=6, column=7, padx=0, pady=10, sticky='nswe', columnspan=1)

        # BOTÕES

        self.botao_criar_cliente = tk.Button(win, text='Cadastrar', command= self._on_cadastrar_clicked)
        self.botao_criar_cliente.grid(row=7, column=2, padx=0, pady=10, sticky='nswe', columnspan=4)

    def _on_cadastrar_clicked(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nomedocliente.get()
        telefone = self.entry_telefone.get()
        logradouro = self.entry_logradouro.get()
        numero = self.entry_numero.get()
        complemento = self.entry_complemento.get()
        bairro = self.entry_bairro.get()
        cidade = self.entry_cidade.get()
        estado = self.combobox_selecionar_estado.get()
        cep = '00000000'


        DAOCliente.cadastrarEndereco(self='self', logradouro=logradouro, numero=numero, bairro=bairro, complemento=complemento,
                                   cidade=cidade, estado=estado, cep=cep)
        print(f"logradouro='{logradouro}' AND numero='{numero}' AND bairro='{bairro}' AND complemento='{complemento}' AND cidade='{cidade}' AND estadp='{estado}' AND cep='{cep}'")

        idk_endereco = DAOCliente.lendobd(self='self',tabela="Endereco",dados=f"logradouro='{logradouro}' AND numero='{numero}' AND bairro='{bairro}' AND complemento='{complemento}' AND cidade='{cidade}' AND estadp='{estado}' AND cep='{cep}'")
        DAOCliente.cadastrarCliente(self='self', cpf=cpf, nome=nome, telefone=telefone, id_endereco=idk_endereco[0][0])

        self.entry_cpf.delete("0", "end")
        self.entry_nomedocliente.delete("0", "end")
        self.entry_telefone.delete("0", "end")
        self.entry_logradouro.delete("0", "end")
        self.entry_numero.delete("0", "end")
        self.entry_complemento.delete("0", "end")
        self.entry_bairro.delete("0", "end")
        self.entry_cidade.delete("0", "end")





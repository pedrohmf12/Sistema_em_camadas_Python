from tkinter import *
from tkcalendar import Calendar
from persistencia.DAOIncidentes import *


class Inci:
    def __init__(self, win):

        # -|- Nome do Atendente

        lbCpf = Label(win, text='CPF ')
        lbCpf.place(relx = 0.02, rely = 0.06)

        entCpf = Entry(win)
        entCpf.place(relx = 0.08, rely = 0.06,relwidth = 0.16,relheight=0.11)

        #GRAU
        def sel():
           print(radio.get())
        radio = IntVar()
        lbGrau = Label(win, text='Grau ')
        lbGrau.place(relx = 0.25, rely = 0.06)

        R1 = Radiobutton(win, text="Grave", value=1, variable=radio,
                          command=sel)
        R1.place(relx = 0.32, rely = 0.06)

        R2 = Radiobutton(win, text="Mediano", value=2,variable=radio,
                          command=sel)
        R2.place(relx = 0.42, rely = 0.06)

        R3 = Radiobutton(win, text="Leve", value=3,variable=radio,
                          command=sel)
        R3.place(relx = 0.55, rely = 0.06)

        lbtxt = Label(win,text='Relato')
        lbtxt.place(relx = 0.02, rely = 0.2)
        inputtxt = Text(win, height =5, width = 65)
        inputtxt.place(relx = 0.03, rely = 0.32)
        def salvarDados():

            try:
                grau = ''
                if radio.get() == 1:
                    grau = 'Leve'
                elif radio.get() == 2:
                    grau = 'Mediano'
                elif radio.get() == 3:
                    grau = 'Grave'
                cpf = entCpf.get()
                data = cal.get_date()
                relato = inputtxt.get(1.0, "end-1c")
                print("Ate")
                DAOIncidentes.inserirdbIncidente(self=self, d1=grau, d2=cpf, d3=data, d4=relato)
                print("Ate2")
                entCpf.delete("0", "end")
                inputtxt.delete("1.0", "end")
            except:pass



        cal = Calendar(win, selectmode='day')
        def grad_date():
            cal.place(relx=0.20, rely=0)
            abrir_cal.place(relx=1000, rely=1000)
            fechar_cal.place(relx=0.79, rely=0.06)

        def grad_date_close():
            cal.place(relx=1000, rely=1000)
            abrir_cal.place(relx=0.79, rely=0.06)
            fechar_cal.place(relx=1000, rely=1000)
            print(cal.get_date())
            lbdata = Label(win,text=f'{cal.get_date()}')
            lbdata.place(relx=0.68, rely=0.07)
            return cal.get_date()
        abrir_cal=Button(win, text="Selecionar data", command=grad_date)
        abrir_cal.place(relx=0.79, rely=0.06)
        fechar_cal=Button(win, text="Escolher data", command=grad_date_close)
        fechar_cal.place(relx=1000, rely=1000)
        buttonSalvar=Button(win, text="Cadastrar", command=salvarDados)
        buttonSalvar.place(relx=0.84, rely=0.83)

        win.geometry("570x180")
        win.resizable(width=0,height=0)

        #messagebox.showerror("Teste","Teste2")






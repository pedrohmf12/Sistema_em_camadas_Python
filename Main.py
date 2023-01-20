import tkinter
from Menu import Menu


class Application:
    def __init__(self):
        window = tkinter.Tk()
        window.minsize(1024, 1024)
        mb = Menu(window)
        window.title('Sistema de Registro de Incidentes')
        window.geometry('{}x{}+0+0'.format(*window.maxsize()))
        window.configure(background='grey')
        window.mainloop()


if __name__ == '__main__':
    Application()
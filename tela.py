from tkinter import *

class Tela:
    def __init__(self, tela):
        self.ini1 = Frame(tela)
        self.ini1.pack()

        self.t1 = Entry(self.ini1, text = "USER")
        self.t1.pack()

        self.b1 = Button(self.ini1, text = "LOGIN")
        self.b1.pack()

janela = Tk()
Tela(janela)
janela.geometry("150x75")
janela.mainloop()

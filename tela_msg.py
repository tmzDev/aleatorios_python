from tkinter import *

class Tela:
    def __init__(self, tela):
        self.msg1 = Frame(tela)
        self.msg1.pack()

        self.msg2 = Label(self.msg1, text = "mensagem")
        self.msg2.pack()

        self.but1 = Button(self.msg1, text = "Alterar", command = self.troca_mas)

        self.but1.pack()
        
    def troca_mas(self):
        self.msg2["text"] = "mensagem alterada"
        self.msg2.pack()


raiz = Tk()
Tela(raiz)
raiz.geometry("150x100")
raiz.mainloop()

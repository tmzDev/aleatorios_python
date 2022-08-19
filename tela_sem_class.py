from tkinter import *

tela = Tk()
text = Label(tela, text = "Texto de amostra", bg = "pink")
text.pack()

but = Button(tela, text = "enviar")
but.pack()

tela.geometry("150x100")
tela.mainloop()

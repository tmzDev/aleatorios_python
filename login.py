# Login e senha simples com tkinter   admin - admin

from tkinter import *

raiz = Tk()
raiz.title("login")

txt_user = Label(raiz, text = "User : ")
txt_user.grid(column = 0, row = 0)
user = Entry(raiz)
user.grid(column = 2, row = 0)


txt_senha = Label(raiz, text = "password :")
txt_senha.grid(column = 0, row = 1)
passw = Entry(raiz)
passw.grid(column = 2, row = 1)

def senha():
    if user.get() == "admin" and passw.get() == "admin":
        login["text"] = "Acesso Liberado"
    else:
        login["text"] = "Acesso Negado"

bt = Button(raiz, text = "login", command = senha)
bt.grid(column = 2)

login = Label(raiz, text = "")
login.grid()

raiz.geometry("200x90")
raiz.mainloop()

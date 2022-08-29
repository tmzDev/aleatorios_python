# Infos cep com interface grafica

from tkinter import *
import requests

raiz = Tk()
raiz.title("Buscador de CEP")
raiz.geometry("400x250")

lb1 = Label(raiz, text = "digite um CEP")
lb1.place(relx = 0.4, rely = 0.05)

ent = Entry(raiz)
ent.place(relx = 0.35, rely = 0.15)

def rast():
    requi = requests.get(f"https://cep.awesomeapi.com.br/json/{ent.get()}")
    req_dct = requi.json()

    s = f'''Cep : {ent.get()} \nEndereço : {req_dct["address_type"]} {req_dct["address_name"]} \nEstado : {req_dct["state"]}
    Bairro : {req_dct["district"]} \nCidade : {req_dct["city"]} \nDDD : 0{req_dct["ddd"]}'''
    lb2["text"] = s
    
lb2 = Label(raiz, text = "")
lb2.place(relx = 0.3, rely = 0.45)

bt = Button(raiz, text = "pesquisar", command = rast)
bt.place(relx = 0.42, rely = 0.3)
raiz.mainloop()

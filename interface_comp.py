from tkinter import *
from turtle import bgcolor 
import requests

def moedas():
    requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao_dic = requisicao.json()

    dolar = requisicao_dic['USDBRL']['bid']
    euro = requisicao_dic['EURBRL']['bid']
    bitcoin = requisicao_dic['BTCBRL']['bid']

    cot = f'Dolar R$ {float(dolar):.2f} \nEuro R$ {float(euro):.2f} \nBitcoin R$ {float(bitcoin):.2f}.00'
    mostra_cotacao['text'] = cot

tela = Tk()
tela.title('Moedas')

texto_inicial = Label(tela, text = 'Clique para mostrar a cotação')
texto_inicial.grid(column = 0, row = 0, padx= 10, pady= 10)

botao = Button(tela, text = 'cotação', command= moedas)
botao.grid(column = 0, row = 1, padx= 10, pady= 10)

mostra_cotacao = Label(tela, text='')
mostra_cotacao.grid(column =0, row = 2)


tela.mainloop()

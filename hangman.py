## Jogo simples de forca

import random

times = ['corinthians', 'palmeiras', 'santos', 'flamengo', 'vasco', 'botafogo', 'fluminense', 'portuguesa', 'gremio',
'internacional', 'vitoria', 'bahia', 'caxias', 'sport', 'nautico', 'cuaiaba', 'bragantino', 'chapecoense', 'figueirense']

time = random.choice(times)

letras_certas = []

while True:
    l = input('Digite uma letra : ').lower()
    if l in time:
        letras_certas.append(l)

    time_temp = ''
    
    for i in time:
        if i in letras_certas:
            time_temp += i
        else:
            time_temp += '_'
    print(time_temp)
    if time_temp == time:
        break
print(f'\nObrigado por jogar! :D')

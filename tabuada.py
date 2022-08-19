import random

while True:
    n = input('Informe um numero para tabuada [a - numero aleatorio] : ')
    if n == 'a':
        num = random.randint(1, 100)
        for i in range(1, 11):
            print(f'{i: <2} x {num} = {num * i}')
    else:
        for i in range(1, 11):
            print(f'{i: <2} x {n} = {i * int(n): <3}')
    op = input('Continuar? [n - sair] : ').lower()
    if op == 'n':
        print('Obrigado :D')
        break

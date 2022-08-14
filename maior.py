# Maior numero

maior = 0
for i in range(1, 6):
    n = int(input('Digite um numero : '))
    if n > maior:
        maior = n
print(f'O maior numero digitado foi {maior}')

cpf_original = input('Digite seu cpf sem traços : ')

cpf = cpf_original[:-2]
cont = 0
x = 10
for i in cpf:
    cont += x * int(i)
    x -= 1
if 11 - (cont % 11) > 9:
    cpf += '0'
else:
    n1 = 11 - (cont % 11)
    cpf += str(n1)


cont2 = 0
y = 11
for i in cpf:
    cont2 += y * int(i)
    y -= 1
if 11 - (cont2 % 11) > 9:
    cpf += '0'
else:
    n2 = 11 - (cont2 % 11)
    cpf += str(n2)

if cpf_original == cpf:
    print(f'{cpf} é um cpf valido')
else:
    print(f'{cpf_original} não é valido')

    

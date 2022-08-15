value = []
while True:
    with open('products.txt', 'a') as arqui:
        n = input('Product : ')
        v = float(input('Value : '))
        q = int(input('Qtd : '))

        value.append(v * q)

        arqui.write(f'Produto {n} - Valor R${v:.2f} Quantidade {q} \n')
    cont = input('Deseja cadastrar mais? [s/n] : ').lower()
    if cont == 'n':
        with open('products.txt') as ler:
            for i in ler:
                print(i)
        break
print(f'Sua lista de produtos no valor de R${sum(value)}')

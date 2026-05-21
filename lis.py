listapr = []
listapar = []
listaimp = []
while True:
    n = int(input('Digite um número: '))
    
    listapr.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimp.append(n)

    sn = ''
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
        
print(f'Ao todo, os números digitados foram {listapr}')
print(f'Os números pares digitados foram {listapar}')
print(f'Os números ímpares digitados foram {listaimp}')
lista = []
cont = 0
five = ''
while True:
    n = int(input('Digite um número: '))

    cont += 1

    lista.append(n)

    sn = ''    
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sn == 'N':
        break

lista.sort(reverse=True)
print(f'{cont} números foram digitados')
print(f'{lista}')

if 5 in lista:
    print('O valor 5 está na lista e foi digitado ')
else:
    print('O valor 5 não foi digitado ')
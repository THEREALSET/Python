tot = list()
cont = 0
pes = list()
dadop = list()
lev = list()
while True:
    name = str(input('Digite nome: '))
    peso = float(input('Digite peso: [Kg]'))
    cont += 1
    dado.append(name)
    dado.append(peso)

    if peso >= 100:
        pes.append(dado[:])
    else:
        lev.append(dado[:])
    dado.clear()
    
    sn = ''
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
print(f'Ao todo, você cadastrou {cont} pessoas. ')
print(f'O maior peso foi de {}Kg. Peso de {}')
print(f'O menor peso foi de {}Kg. Peso de {}')
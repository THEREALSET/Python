tot = 0
prodk = 0
while True:
    name = str(input('Nome do produto: ')).strip().lower()
    prec = float(input('Preço: R$'))

    while True:
        nex = str(input('Você quer continuar cadastrando produtos? [S/N] ')).strip().upper()[0]
        if nex != 'S' and nex != 'N':
            nex = str(input('Você quer continuar cadastrando produtos? [S/N] ')).strip().upper()[0]
        else:
            break

    if nex == 'N':
        print('Encerrando...')
        break

    if prec >= 1000:
        tot += 1

    
    tot += prec
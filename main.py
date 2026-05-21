n = ''
tot18 = 0
toth = 0
totf20 = 0
while True:
    ida = int(input('Idade: '))

    sex = ''
    while sex not in 'MF':              
            sex = str(input('Sexo: [M/F] ')).strip().upper()[0]   

    if ida >= 18:
        tot18 += 1

    if sex == 'M':
        toth += 1

    if sex == 'F' and ida < 20:
        totf20 +=1    

    n = ''
    while n not in 'SN':
            n = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    
    if n == 'N':
        print('Encerrando...')
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo, temos {toth} homens cadastrados')
print(f'E temos {totf20} mulheres com menos de 20 anos')
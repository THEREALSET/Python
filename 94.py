lista = []
pessoa = {}
while True:
    pessoa['name'] = str(input('Nome: ')).strip()

    sex = ''
    while sex not in ['M', 'F']:
        sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['sex'] = sex
    
    idade = -1
    while idade < 0:
        idade = int(input('Idade: '))
    pessoa['idade'] = idade
    med = 0
    med += idade
    
    lista.append(pessoa.copy())
    pessoa.clear()

    sn = ''
    while sn not in ['S', 'N']:
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
        
med = med / len(lista)
print(f'- O grupo tem {len(lista)} pessoas. ')
print(f'- A média de idade é de {med} anos. ')
muj = []
for mu in lista:
    if pessoa['sex'] == 'F':
        muj.append(mu['name'])
print(f'- As mulheres cadastradas foram: {", ".join(muj)}')
print(f'- Lista das pessoas que estão acima da média: ')
for people in lista:
    if idade > med:
        print(people)
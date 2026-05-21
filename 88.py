from random import randint
lista = []
jg = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for z in range(jogos):
    for x in range(6):
        jg.append(randint(1, 60))
    lista.append(jg[:])
    jg.clear()
print(f'Sorteando {jogos} jogos')
for j in range(jogos):
    print(f'Jogo {j + 1}: {lista[j]}')
print('Boa Sorte!')
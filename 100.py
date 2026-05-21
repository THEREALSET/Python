from random import randint
numeros = []
def sorteia():
    for x in range(5):
        numeros.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: {numeros} PRONTO! ')
def somaPar():
    soma = 0
    for x in numeros:
        if x % 2 == 0:
            soma += x
    print(f'Somando so valores pares de {numeros}, temos {soma} ')
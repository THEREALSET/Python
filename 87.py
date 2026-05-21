matriz = [[], [], []]  # Inicializa a matriz com três listas vazias
par = 0
soma3 = 0
for x in range(3):  # Para cada linha
    for i in range(3):  # Para cada coluna
        val = int(input(f'Digite um valor para [{x}, {i}]: '))
        matriz[x].append(val)  # Adiciona o valor à linha correspondente
        if val % 2 == 0:
            par += val
# Exibe a matriz linha por linha
for linha in matriz:
    print(linha)
for x in matriz:
    soma3 += x[2]
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
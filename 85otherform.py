matriz = [[], [], []]  # Inicializa a matriz com três listas vazias

for x in range(3):  # Para cada linha
    for i in range(3):  # Para cada coluna
        val = int(input(f'Digite um valor para [{x}, {i}]: '))
        matriz[x].append(val)  # Adiciona o valor à linha correspondente

# Exibe a matriz linha por linha
for linha in matriz:
    print(linha)

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas.append(int(input(f'Quantas partidas {jogador['nome']} jogou? ')))
gl = tot = 0
for x in range(1, partidas[0] + 1):
    gl = int(input(f'Quantos gols na partida {x}? '))
    tot += gl
    partidas.append(gl)
jogador['gols'] = partidas[1:]
jogador['total'] = tot
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}. ')
print(f'O jogador {jogador['nome']} jogou {partidas[0]} partidas. ')
for z, i in enumerate(partidas, 1):
    if z != 1:
        print(f'Na partida {z - 1}, fez {i} gols.')
print(f'Foi um total de {tot} gols.')
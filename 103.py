def ficha(name='', gols=''):
    if name == '':
        name = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {name} fez {gols}gol(s) no campeonato. ')
nm = str(input('Nome do jogador: '))
gl = str(input('Número de gols: '))
ficha(nm, gl)
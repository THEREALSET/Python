def voto(ano):
    if ano < 16:
        return 'NÃO VOTA. '
    elif ano >= 18 and ano < 60:
        return 'VOTO OBRIGATÓRIO. '
    elif ano >= 16 and ano < 18 or ano >= 60:
        return 'VOTO OPCIONAL. '
yea = 2024 - int(input('Em que ano você nasceu? '))

print(f'Com {yea} anos: {voto(yea)}')
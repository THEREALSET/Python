def contador(i, f, p):
    res = []
    if p == 0:
        p = 1
    if i < f:
        for x in range(i, f + 1, p):
            res.append(x)
    elif i > f and p > 0:
        for x in range(i, f - 1, -p):
            res.append(x)
    elif i > f and p < 0:
        for x in range(i, f - 1, p):
            res.append(x)
    print(res)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez dde personalizar a contagem! ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
print(f'Contagem de {ini} até {fim} de {pas} em {pas} ')
contador(ini, fim, pas)
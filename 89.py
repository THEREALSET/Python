boletim = []
aluno = []
while True:
    name = str(input('Nome: ')).strip()
    not1 = float(input('Nota 1: '))
    not2 = float(input('Nota 2: '))

    aluno.append(name)
    aluno.append((not1 + not2) / 2)
    aluno.append(not1)
    aluno.append(not2)
    boletim.append(aluno[:])
    aluno.clear()

    sn = ''
    while sn not in ['S', 'N']:
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
print('BOLETIM ESCOLAR ')
print('num')
for i, al in enumerate(boletim):
    nome = al[0]
    med = al[1]
    print(f'{i}    {nome} {med}')
while True:
    esp = int(input('Mostrar notas de qual aluno? (-1 interrompe): '))
    print(f'Notas de {boletim[esp][0]} são {boletim[esp][2:]}')
    if esp == -1:
        break
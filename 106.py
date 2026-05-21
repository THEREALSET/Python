def escreva(a):
    print('~' *(len(a) + 4))
    print('{:^{}}'.format(a, len(a) + 4))
    print('~' *(len(a) + 4))

while True:
    print(escreva('SISTEMA DE AJUDA PyHELP'))
    fn = str(input('Função ou Biblioteca > ')).strip()
    
    escreva(f'Acessando o manual do comando '{fn}'')
    help(fn)

    if fn.upper() == 'FIM':
        break
escreva('ATÉ LOGO!')
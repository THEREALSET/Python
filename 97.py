def escreva(a):
    print('~' *(len(a) + 4))
    print('{:^{}}'.format(a, len(a) + 4))
    print('~' *(len(a) + 4))
escreva('uiuiui')
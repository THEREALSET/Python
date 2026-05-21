larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
def area(a, b):
    print(a * b)
val = area(larg, comp)
print(f'A área de um terreno {larg}x{comp} é de {val}m2.')
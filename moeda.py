def moeda(n, show=False):
    return f'R${n:.2f}'.replace('.', ',')

def aumentar(n, val, show=False):
    """Aumenta o valor `n` em uma porcentagem `val`."""
    res = n + (n*val/100)
    if show:
        return moeda(res)
    else:
        return res

def diminuir(n, val, show=False):
    """Diminui o valor `n` em uma porcentagem `val`."""
    res = n - (n*val/100)
    if show:
        return moeda(res)
    else:
        return res

def dobro(n, show=False):
    """Retorna o dobro do valor `n`."""
    res = n*2
    if show:
        return moeda(res)
    else:
        return res

def metade(n, show=False):
    """Retorna a metade do valor `n`."""
    res = n/2
    if show:
        return moeda(res)
    else:
        return res

def resumo(n, au=10, re=10):
    print('-'*30)
    print('RESUMO DO VALOR ')
    print('-'*30)
    print(f'Preço analisado: {moeda(n)} ')
    print(f'Dobro do preço: {dobro(n, show=True)} ')
    print(f'Metade do preço: {metade(n, show=True)} ')
    print(f'{au}% de aumento: {aumentar(n, au, show=True)} ')
    print(f'{re}% de redução: {diminuir(n, re, show=True)} ')

def leiaDinheiro(num):
    while True:
        ent = str(input(num)).replace(',', '.').strip()
        if ent.isalpha() or ent == '':
            print('Erro')
        else:
            return float(ent)
            break

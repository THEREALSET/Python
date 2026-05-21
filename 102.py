def fatorial(n, show=False):
    """
    Calculadora de fatoriais.

    :param n: Número a ser calculado o fatorial
    :param show: (Opcional) Mostra ou não o processo de calculo
    return: O valor do fatorial de n.
    """
    p = 1
    for x in range(n, 0, -1):
        p *= x
        if show:
            print(f'{x} {'x ' if x > 1 else '= '}', end='')
    return p
print(fatorial(5, show=False))
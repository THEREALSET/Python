def notas(* num, sit=False):
    nt = {}
    nt['total'] = len(num)
    nt['maior'] = max(num)
    nt['menor'] = min(num)
    nt['média'] = sum(num) / len(num)
    if sit:
        if nt['média'] >= 7.0:
            nt['situação'] = 'BOA'
        elif nt['média'] < 7.0 and nt['média'] > 5.0
            nt['situação'] = 'RAZOÁVEL'
        else:
            nt['situação'] = 'RUIM'
    return nt
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
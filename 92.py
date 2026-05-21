pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
while True:
    pessoa['idade'] = 2024 - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
print(pessoa.items())
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] - (2024 - pessoa['idade'])) + 35
    print(f'nome tem o valor {pessoa['nome']} ')
    print(f'idade tem o valor {pessoa['idade']} ')
    print(f'CTPS tem o valor {pessoa['CTPS']} ')
    print(f'contratação tem o valor {pessoa['contratação']} ')
    print(f'salário tem o valor {pessoa['salário']} ')
    print(f'aposentadoria tem o valor {pessoa['aposentadoria']} ')
else:
    print(f'nome tem o valor {pessoa['nome']} ')
    print(f'idade tem o valor {pessoa['idade']} ')
    print(f'CTPS tem o valor {pessoa['CTPS']} ')
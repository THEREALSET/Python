# Para valores de centenas+ ou com as casas das dezenas em 5, use a cédula de 50
# Para valores de dezenas com números pares, use a cédula de 20
# Para valores de dezenas que não foram completos com as de 20, adicione 1 nota de 10
# Para os valores das unidade, use a moeda de 1 real
#val % 50 // 20
#val % 20 // 10
#val % 10 // 1
val = 0.1
while val % 1 != 0 or val < 0:
    val = int(input('Valor que deseja sacar(Não sacamos centavos): '))

print(f'Total de {val // 50} cédulas de R$50')
print(f'Total de {(val % 50) // 20} cédulas de R$20')
print(f'Total de {((val % 50) % 20) // 10} cédulas de R$10')
print(f'Total de {(((val % 50) % 20) % 10) // 1} moedas de R$1')
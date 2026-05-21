lista = []
for i in range(5):
    n = int(input('Digite um valor: '))

    if not lista: # se a lista estiver vazia
        lista.append(n)
        print('Adicionado ao final da lista... ')
    else:
        for x in range(len(lista)):
            if n < lista[x]: #encontrou a posição para inserir
                lista.insert(x, n)
                print(f'Adicionado a posição {x} da lista... ')
                break
        else:
                lista.append(n) # não encontrou a posição
                print('Adicionado ao final da lista.. ')
print(f'Os valores digitados em ordem foram {lista}')
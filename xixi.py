with open("numeros.txt", "w") as arquivo:
    for x in range(1, 9999):
        if x < 10:
            arquivo.write(f'000{x}\n')
        elif x < 100:
            arquivo.write(f'00{x}\n')
        elif x < 1000:
            arquivo.write(f"0{x}\n")
        else:
            arquivo.write(f'{x}\n')
print("Números salvos em 'numeros.txt'")
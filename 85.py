lin0 = []
lin1 = []
lin2 = []
for x in range(3):
    for i in range(3):
        val = int(input(f'Digite um valor para [{x}, {i}]: '))
        if len(lin0) < 3:
            lin0.append(val)
        elif len(lin1) < 3:
            lin1.append(val)
        elif len(lin2) < 3:
            lin2.append(val)
print(lin0)
print(lin1)
print(lin2)
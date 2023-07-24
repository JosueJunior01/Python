total = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        total = total + c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {total}')

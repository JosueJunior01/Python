num = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11):
    multiplier = num * i
    print(f'{num} x {i} = {multiplier}')

print('=' * 12)
print('10 TERMOS DA PA')
print('=' * 12)

firstTerm = int(input('Primeiro termo: '))
reasonPA = int(input('Razão: '))
cont = 1

while cont < 11:
    print(firstTerm, end='  ')
    firstTerm += reasonPA
    cont += 1
print('ACABOU')
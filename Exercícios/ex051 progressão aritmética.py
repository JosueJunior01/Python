print('=' * 12)
print('10 TERMOS DA PA')
print('=' * 12)

firstTerm = int(input('Primeiro termo: '))
reasonPA = int(input('Razão: '))

for i in range(1, 11):
    print(firstTerm, end='  ')
    firstTerm += reasonPA
print('ACABOU')
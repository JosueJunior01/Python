print('=' * 12)
print('10 TERMOS DA PA')
print('=' * 12)

firstTerm = int(input('Primeiro termo: '))
reasonPA = int(input('Razão: '))
cont = 1
more = 10
total = 0
while more != 0:
    total += more
    while cont <= total:
        print(firstTerm, end='  ')
        firstTerm += reasonPA
        cont += 1
    print('PAUSA')
    more = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Finalizando o programa com {total} termos mostrado')

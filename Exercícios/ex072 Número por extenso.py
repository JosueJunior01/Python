num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

escolha = int(input('Escolha um número de 0 a 10: '))

if escolha >= 0 and escolha <= 10:
    print(f'Voce escolheu o número {num[escolha]}')
else:
    print('Número invalido')
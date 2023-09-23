from math import factorial

num = int(input('Digite um número para\n'
                'calcular o fatorial: '))
cont = num

print(f'Calculando {num}! =', end=' ')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print(factorial(num))

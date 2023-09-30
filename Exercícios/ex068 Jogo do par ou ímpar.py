from random import randint

count = 0

print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)

while True:
    num = int(input('Digite um valor: '))

    computador = randint(1, 10)
    soma = num + computador
    escolha = ' '
    
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        
    print(f'Voce jogou {num} e o computador jogou {computador}. Total de {soma}.')
    
    if escolha == 'P':
        if soma % 2 == 0:
            print('Voce venceu!!')
            count += 1
        else:
            print('Voce perdeu!!')
            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print('Voce perdeu!!')
            break
        else:
            print('Voce venceu!!')
            count += 1
            
    print('Vamos jogar novamente...')

print(f'GAME OVER! Voce venceu {count} vezes.')

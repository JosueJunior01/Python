from time import sleep

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

while True:
    print('[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR NÚMERO\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGRAMA')
    choice = int(input('Qual sua opção? '))
    if choice == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1 + n2}')
    elif choice == 2:
        print(f'A multiplicação de {n1} e {n2} é igual a {n1 * n2}')
    elif choice == 3:
        print(f'O maior número entre os dois é {max(n1, n2)}')
    elif choice == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif choice == 5:
        print('Finalizando...')
        sleep(3)
        print('Fim do programa, volte sempre!')
        break
    else:
        print('Opção inválida. Por favor escolha uma opção válida')
    print('-=' * 12)

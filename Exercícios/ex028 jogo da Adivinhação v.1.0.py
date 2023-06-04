from random import choice
from time import sleep

print('-=' * 30)
print('Vou pensar num número de 1 a 5, tente adivinhar. Mas antes, quero saber seu nome')
name = str(input('Nome: ')).strip().title()
print('-=' * 30)
machineNumber = [1, 2, 3, 4, 5]
machineWins = userWins = 0
winner = ''

while True:
    print('Vamos começar!!!')
    sleep(1)
    for i in range(0, 5):
        randomNumber = choice(machineNumber)
        number = int(input('Em qual número eu pensei? '))
        print('PROCESSANDO...')
        if number == randomNumber:
            print('PARABÉNS, VOCÊ ACERTOU!!!!!')
            userWins += 1
        else:
            print('Essa não... Número errado!')
            machineWins += 1
        sleep(.5)
        print(f'O número que escolhi foi {randomNumber}\n')
        sleep(.5)
    if userWins > machineWins:
        print('\033[34mO vencedor foi VOCÊ! Parabéns!!!!\033[m')
        winner = name
    else:
        print('\033[34mO vencedor foi a MÁQUINA! Lamento...\033[m')
        winner = 'Máquina'
    print(f'A pontuação foi {userWins}X{machineWins} para {winner}.')
    tryAgain = str(input('Gostaria de tentar novamente? [Sim/Não] ')).strip().lower()
    if tryAgain in 'não, nao, n':
        break

print('Achei divertido! Até a próxima <3')

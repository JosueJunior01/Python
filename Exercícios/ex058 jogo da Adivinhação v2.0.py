from random import randint

num = randint(0, 10)
player = ''
cont = 0

print('Sou seu computador...\n'
      'acabei de pensar em um número de 0 a 10\n'
      'Será que consegue adivinhar qual foi?')

while player != num:
    player = int(input('Qual o seu palpite? '))
    if player < num:
        print('Mais... Tente mais uma vez')
    elif player > num:
        print('Menos... Tente mais uma vez')
    cont += 1

print(f'Acertou com {cont} tentativas')
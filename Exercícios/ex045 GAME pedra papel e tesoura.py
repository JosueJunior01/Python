from time import sleep
from random import randint

jokenpo = ['Pedra', 'Papel', 'Tesoura']
machineChoice = randint(0, 2)

print('Suas opções:\n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')

playerChoice = int(input('Qual é a sua jogada? '))

print('JO')
sleep(.5)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print(f'Computador jogou {jokenpo[machineChoice]}')
print(f'Você jogou {jokenpo[playerChoice]}')
print('-=' * 11)

if machineChoice == 0:
      if playerChoice == 0:
            print('Deu empate')
      elif playerChoice == 1:
            print('Você venceu!')
      elif playerChoice == 2:
            print('Você perdeu!')
      else:
            print('Opção inválida!!!')
elif machineChoice == 1:
      if playerChoice == 0:
            print('Você perdeu!')
      elif playerChoice == 1:
            print('Deu empate')
      elif playerChoice == 2:
            print('Você venceu!')
      else:
            print('Opção inválida!!!')
elif machineChoice == 2:
      if playerChoice == 0:
            print('Você venceu!')
      elif playerChoice == 1:
            print('Você perdeu!')
      elif playerChoice == 2:
            print('Deu empate')
      else:
            print('Opção inválida!!!')

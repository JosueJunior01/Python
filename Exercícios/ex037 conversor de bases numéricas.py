num = int(input('Difite um número inteiro: '))
print('Escolha uma das bases para conversão: \n[1] converter para BINÁRIO\n'
      '[2] converter para OCTAL\n'
      '[3] Converter para HEXADECIMAL')
chosenOption = int(input('Sua opção: '))
if chosenOption == 1:
    binary = bin(num)
    print('{} convertido para BINÁRIO é igual a {}'.format(num, binary[2:]))
elif chosenOption == 2:
    octal = oct(num)
    print('{} convertido para OCTAL é igual a {}'.format(num, octal[2:]))
elif chosenOption == 3:
    hexadecimal = hex(num)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hexadecimal[2:]))
else:
    print('Opção INVÁIDA, tente novamente')

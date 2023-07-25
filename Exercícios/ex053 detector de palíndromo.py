phrase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')

print(f'O inverso de {phrase} é {phrase[::-1]}')

if phrase == phrase[::-1]:
    print('Temos um palíndromo!')
else:
    print('Isso não é um palíndromo!')

num = int(input('Informe um número: '))
numberUnit = num // 1 % 10
dozensNumber = num // 10 % 10
hundredsNumber = num // 100 % 10
thousandsNumber = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidades: {numberUnit}')
print(f'Dezenas: {dozensNumber}')
print(f'Centenas: {hundredsNumber}')
print(f'Milhares: {thousandsNumber}')

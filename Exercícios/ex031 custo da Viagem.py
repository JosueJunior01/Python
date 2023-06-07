tripDistance = int(input('Qual a disntância da viagem? '))
print(f'Você está prestes a realizar uma viagem de {tripDistance}Km')
if tripDistance <= 200:
    price = tripDistance * 0.50
else:
    price = tripDistance * 0.45
print('O valor da viagem vai custar R${:.2f} ao total'.format(price))
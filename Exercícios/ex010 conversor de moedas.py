# Considerando US$ 1.00 = R$ 3,27
carteira = float(input('Quanto você tem na carteira? '))
dolar = 1.00
reais = 3.27
convertido = (carteira / reais) / dolar
print('Com R$ {} você consegue US$ {:.2f}'.format(carteira, convertido))

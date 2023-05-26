# Cada litro de tinta, pinta 2m quadrados
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura

print(f'As dimensões da parede são {largura}m de largura e {altura}m de altura')

tinta = area / 2

print('Para pintar {}m², vai precisar de {:.2f}l'.format(area, tinta))
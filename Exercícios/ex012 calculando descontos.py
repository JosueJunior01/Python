preço = float(input('Qual o preço do produto? '))
desconto = preço - (preço * 5 / 100)

print('O que custava {}, com o desconto de 5% vai sair por {:.1f}.'.format(preço, desconto))
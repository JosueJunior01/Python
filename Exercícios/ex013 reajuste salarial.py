salario = float(input('Qual o salário do funcionário? R$ '))
print('Um funcionário que ganhava R${:.2f}, com o ajuste de 15% de aumento, passa a ganhar {:.2f}'.format(salario, salario + (salario * 15 / 100)))

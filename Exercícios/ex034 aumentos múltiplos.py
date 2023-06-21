# Aumentar o salário em 15% para salários abaixo ou igual a R$1250,00
# Para superiores, o salário aumenta 10%.
wage = float(input('Qual o salário do funcionário? R$'))

if wage <= 1250:
    salaryIncrease = wage + (wage * 15 / 100)
else:
    salaryIncrease = wage + (wage * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganhar {:.2f} agora.'.format(wage, salaryIncrease))

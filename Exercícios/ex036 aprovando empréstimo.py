housePrice = float(input('Qual o valor da casa? R$'))
salary = float(input('Salário do comprador: R$'))
yearsFunding = int(input('Quantos anos de financiamento? '))
monthlyInstallment = housePrice / (yearsFunding * 12)
minimumInstallment = salary * (30 / 100)

print('Para pagar uma casa de {:.2f} em {} anos, a prestação será de {:.2f} reais'.format(housePrice, yearsFunding, monthlyInstallment))

if monthlyInstallment <= minimumInstallment:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

print('========== CAFETERIA DO JÚNIOR ==========')

shoppingPrice = float(input('Preço das compras: R$ '))

print('Formas de Pagamento')
print('[1] à vista dinheiro/cheque\n'
      '[2] à vista cartão\n'
      '[3] 2x no cartão\n'
      '[4] 3x ou mais no cartão')

chosenOption = int(input('Qual opção? '))

if chosenOption == 1:
    discount = shoppingPrice - (shoppingPrice * 10 / 100)
    print('Sua compra de {:.2f} vai custar {:.2f} com 10% de desconto.'.format(shoppingPrice, discount))
elif chosenOption == 2:
    discount = shoppingPrice - (shoppingPrice * 5 / 100)
    print('Sua compra de {:.2f} vai custar {:.2f} com 10% de desconto.'.format(shoppingPrice, discount))
elif chosenOption == 3:
    payment_times = shoppingPrice / 2
    print('Sua compra de {:.2f} será parcelada em 2 vezes de {:.2f} no cartão sem juros.'.format(shoppingPrice, payment_times))
elif chosenOption == 4:
    interestRate = shoppingPrice + (shoppingPrice * 20 / 100)
    payment_times = int(input('Em quantas parcelas deseja pagar? '))
    installments = interestRate / payment_times
    print('Sua compra será parcelada em {} vezes de R${:.2f} com juros'.format(payment_times, installments))
    print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(shoppingPrice, interestRate))
else:
    print('Opção INVÁLIDA de pagamento. Tente novamente')

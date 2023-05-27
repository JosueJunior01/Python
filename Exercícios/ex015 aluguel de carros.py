# Cada dia custa R$60 e cada Km custa R$0,15
dia = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quanto Km rodados? '))
somaTotal = (dia * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(somaTotal))

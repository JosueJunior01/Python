print('=' * 30)
print(f'{"Banco JR":^30}')
print('=' * 30)

valorSacar = int(input('Qual valor voc deseja sacar? R$'))

total = valorSacar
celula = 50
totalCelulas = 0

while True:
    if total >= celula:
        total -= celula
        totalCelulas += 1
    else:
        if totalCelulas > 0:
            print(f'Total dr {totalCelulas} células de R${celula}')
        if celula == 50:
            celula = 20
        elif celula == 20:
            celula = 10
        elif celula == 10:
            celula = 5
        elif celula == 5:
            celula = 1
        totalCelulas = 0
        if total == 0:
            break
print('Tenha um bom dia!')
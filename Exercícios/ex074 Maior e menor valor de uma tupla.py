from random import choice

num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
count = 1
maiorValor = menorValor = 0

print('Os numeros sorteados foram: ', end='')

for c in range(1, 6):
    sorteio = choice(num)
    print(sorteio, end=' ')
    if count == 1:
        maiorValor = menorValor = sorteio
    else:
        if maiorValor < sorteio:
            maiorValor = sorteio
        elif menorValor > sorteio:
            menorValor = sorteio
    count += 1

print(f'\nO maior valor foi {maiorValor}')
print(f'O menor valor foi {menorValor}')

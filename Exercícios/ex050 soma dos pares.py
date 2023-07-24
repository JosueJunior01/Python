addition = 0
cont = 0

for i in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        addition += num
        cont += 1
print(f'Dos 6 números solicitados {cont} deles são pares e a soma entre eles é {addition}')

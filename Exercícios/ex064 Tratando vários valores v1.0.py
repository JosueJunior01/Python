soma = count = 0


while True:
    num = int(input('Digite um número [999 para parar]'))
    if num == 999:
        break
    soma += num
    count += 1
    
print(f'Voce digitou {count} números. A soma entre eles é {soma}.')
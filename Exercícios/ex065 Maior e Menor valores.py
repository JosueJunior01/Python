count = soma = maior = menor = media = 0

while True:
    num = int(input('Digite um número: '))
    count += 1
    
    if count == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    
    soma += num
    
    pergunta = str(input(' Quer continuar? [S/N] '))[0].upper().strip()
    if pergunta == 'N':
        break
    elif pergunta == 'S':
        continue
    else:
        print('Resposa inválida.')
        pergunta = str(input(' Quer continuar? [S/N] '))[0].upper().strip()
        if pergunta == 'S':
            continue
        else:
            break

media = soma / count

print(f'Voce digitou {count} números e a média foi {media:.2f}.\nO maior valor foi {maior} e o menor foi {menor}')

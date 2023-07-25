num = int(input('Digite um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[33m{i}', end=' ')
        total += 1
    else:
        print(f'\033[31m{i}', end=' ')

print(f'\n\033[mO número {num} foi divisível {total} vezes')

if total == 2:
    print('Ele É um número PRIMO')
else:
    print('Ele NÃO É um número PRIMO')

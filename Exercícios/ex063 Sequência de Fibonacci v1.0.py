print('~' * 25)
print('Sequência de Fibonacci')
print('~' * 25)

num = int(input('Quantidade de termos que deseja mostrar: '))

if num >= 1:
    print('1', end=' ')

penultimo = 0
ultimo = 1
count = 1

while count < num:
    termo = ultimo + penultimo
    print(termo, end=' ')
    penultimo = ultimo
    ultimo = termo
    count += 1
    
print('FIM')
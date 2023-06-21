num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

smaller = num1
bigger = num3

if num2 < num1 and num2 < num3:
    smaller = num2
if num3 < num1 and num3 < num2:
    smaller = num3
if num1 > num2 and num1 > num3:
    bigger = num1
if num2 > num1 and num2 > num3:
    bigger = num2
print(f'O menor valor é {smaller} e o maior valor é {bigger}')

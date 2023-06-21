# Dada as medidas de 3 lados, a soma dos dois lados menores deve ser maior que o lado que restou
# Se a soma der igual ou menor, não é possível formar triângulos
print('-=' * 30)
print('Analizador de Triângulos')
print('-=' * 30)
num1 = int(input('Digite a medida do primeiro lado: '))
num2 = int(input('Digite a medida do segundo lado: '))
num3 = int(input('Digite a medida do terceiro lado: '))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM formar triângulos')

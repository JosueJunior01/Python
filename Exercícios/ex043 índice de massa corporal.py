weight = float(input('Qual o seu peso? [kg] '))
height = float(input('Qual a sua altura? [m] '))
imc = weight / (height ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO, cuidado!')
elif 18.5 < imc <= 25:
    print('Esse é o PESO IDEAL.')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO, fique atento')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE, cuidado!!!')
else:
    print('Você está com OBESIDADE MÓRBIDA. Procure ajuda')

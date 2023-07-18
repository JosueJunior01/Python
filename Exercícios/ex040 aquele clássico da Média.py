studentGrade01 = float(input('Nota do aluno: '))
studentGrade02 = float(input('Segunda nota do aluno: '))
average = (studentGrade01 + studentGrade02) / 2

if average < 5:
    print(f'Você foi REPROVADO. A média é 5.0 e sua média foi {average}')
elif average >= 5 and average < 7:
    print(f'Você está em RECUPERAÇÃO. A média é 5.0 e sua média foi {average}')
else:
    print(f'Você foi APROVADO. Parabéns!!! Sua média foi {average}')

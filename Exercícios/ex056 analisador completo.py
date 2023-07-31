totalAge = 0
olderMan = ''
olderManAge = 0
underageWomen = 0

for i in range(1, 5):
    print(f'----- {i}ª pessoal -----')
    name = str(input('Nome: ')).title().strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo:[M/F] ')).upper()
    totalAge += age
    if i == 1 and gender == 'M':
        olderMan = name
        olderManAge = age
    elif gender == 'M' and age > olderManAge:
        olderManAge = age
        olderMan = name
    elif gender == 'F' and age < 20:
        underageWomen += 1

averageAge = totalAge / 4

print('A média de idade do grupo é {:.1f}'.format(averageAge))
print(f'O homem mais velho tem {olderManAge} anos e se chama {olderMan}')
print(f'Ao todo são {underageWomen} mulheres com menos de 20 anos')

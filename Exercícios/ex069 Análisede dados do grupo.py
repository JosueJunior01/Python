maioresIdade = numHomens = mulheresMenos20 = count = 0

while True:
    print('=' * 30)
    print('CADASTRE UMA PESSOA')
    print('=' * 30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        maioresIdade += 1
    if sexo == 'M':
        numHomens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    count += 1

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Ao total temos {count} pessoas cadastradas.\n'
      f'Número de pessoas maiores de idade: {maioresIdade}\n'
      f'Homens cadastrados: {numHomens}\n'
      f'Mulheres com menos de 20 anos: {mulheresMenos20}')
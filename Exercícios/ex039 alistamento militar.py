from datetime import date

currentYear = date.today().year
gender = str(input('Qual o seu sexo biológico: [F/M] '))

if gender in 'F, f':
    print('O alistamento obrigatório ao exército não é obrigatório para mulheres no Brasil')
if gender in 'M, m':
    year = int(input('Digite o ano em que você nasceu: '))
    age = currentYear - year
    if age < 18:
        remainingYears = 18 - age
        print(f'Ainda faltam {remainingYears} anos até o alistamento militar')
        print(f'Seu alistamento vai ser no ano {currentYear + remainingYears}')
    elif age > 18:
        pastAge = age - 18
        print(f'O indivíduo ja deve ter se alistado ao exército a {pastAge} anos')
        print(f'Seu alistamento foi no ano {currentYear - pastAge}')
    else:
        print('O indivíduo deve se apresentar esse ano ao exército brasileiro.')
else:
    print('Resposta não identificada. Apenas "F" ou "M"')

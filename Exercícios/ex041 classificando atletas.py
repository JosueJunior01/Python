from  datetime import date

currentYear = date.today().year
year = int(input('Em que ano você nasceu? '))
age = currentYear - year

if age < 9:
    print(f'O atleta tem {age} anos')
    print('CLASSIFICAÇÃO: Mirim')
elif 8 < age < 15:
    print(f'O atleta tem {age} anos')
    print('CLASSIFICAÇÃO: Infantil')
elif 14 < age < 20:
    print(f'O atleta tem {age} anos')
    print('CLASSIFICAÇÃO: Junior')
elif 19 < age < 26:
    print(f'O atleta tem {age} anos')
    print('CLASSIFICAÇÃO: Sênior')
else:
    print(f'O atleta tem {age} anos')
    print('CLASSIFICAÇÃO: Master')

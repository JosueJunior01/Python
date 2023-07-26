from datetime import date

currentYear = date.today().year
under_age = of_legal_age = 0

for people in range(1, 8):
    birth = int(input(f'Em que ano a {people}ª pessoa nasceu? '))
    age = currentYear - birth
    if age < 21:
        under_age += 1
    else:
        of_legal_age += 1
print(f'Ao todo, tivemos {under_age} pessoas menores de idade')
print(f'E também tivemos {of_legal_age} pessoas maiores de idade')

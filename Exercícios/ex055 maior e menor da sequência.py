smallerMass = greaterMass = 0

for i in range(1, 6):
    mass = float(input(f'Qual o peso da {i}ª pessoa? '))
    if i == 1:
        smallerMass = greaterMass = mass
    else:
        if mass < smallerMass:
            smallerMass = mass
        elif mass > greaterMass:
            greaterMass = mass
print(f'O maior peso lido foi {greaterMass}')
print(f'O menor peso lido foi {smallerMass}')

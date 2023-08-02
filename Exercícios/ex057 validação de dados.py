gender = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]

while gender not in 'MF':
    gender = str(input('Dados inválidos. Tente novamente:[M/F] ')).strip().upper()[0]

print(f'Sexo {gender} registrado com sucesso!!!')

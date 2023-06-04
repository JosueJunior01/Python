# Um programa que lê a cidade e verifica se ela começa com "SANTO"

city = str(input('Digite a cidade em que nasceu: ')).strip().lower().split()

print('santo' in city[0])

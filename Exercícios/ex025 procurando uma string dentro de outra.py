# Vai ler o nome de alguém e analisar se tem "SILVA" no nome

name = str(input('Digite seu nome: ')).strip().lower()
print(f'Seu nome tem SILVA? {"silva" in name}')

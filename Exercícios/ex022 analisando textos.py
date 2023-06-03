from time import sleep

name = str(input('Digite seu nome completo: ')).strip()

sleep(1)
print('Analisando...')
sleep(1.5)
print(f'Seu nome em maiúsculo fica {name.upper()}')
sleep(1)
print(f'Seu nome em minúsculo fica {name.lower()}')
sleep(1)
print('Seu nome ao todo tem {} letras'.format(len(name) - name.count(' ')))
sleep(1)
separateName = name.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separateName[0], len(separateName[0])))

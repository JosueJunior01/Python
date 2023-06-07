carSpeed = int(input('Qual a velocidade do carro? '))
limitSpeed = 80
if carSpeed < limitSpeed:
    print('\033[33mTenha um bom dia, dirijá com cuidado!')
else:
    trafficTicket = float((carSpeed - limitSpeed) * 7)
    print(f'\033[31mMULTADO! Você passou do limite de velocidade de 80Km/h, a multa será de R${trafficTicket}')
    print('\033[33mDirija com cuidado.')

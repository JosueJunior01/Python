totalGastos = produtosMaisDeMil = count = 0

produtoMaisBarato = float('inf')  # Inicializado com um valor infinito
nomeProdutoBarato = ''

while True: 
    print('=' * 30)
    print('Lojas Baratão')
    print('=' * 30)
    
    nomeProduto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    
    count += 1
    totalGastos += valor
    
    if valor >= 1000:
        produtosMaisDeMil += 1
    
    if valor < produtoMaisBarato:
        produtoMaisBarato = valor
        nomeProdutoBarato = nomeProduto
    
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    
    if continuar == 'N':
        break

print(f'O total de gastos nas compras foi de R$ {totalGastos:.2f}\n'
      f'A quantidade de produtos com mais de R$ 1.000 foi {produtosMaisDeMil}\n'
      f'O produto mais barato foi {nomeProdutoBarato} custando R$ {produtoMaisBarato:.2f}')
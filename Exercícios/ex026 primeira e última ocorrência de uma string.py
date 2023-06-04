phrase = str(input('Digite uma frase: ')).strip().lower()

print(f'A letra "A" aparece {phrase.count("a")} vezes na frase')
print(f'A primeira letra "A" aparece na posição {phrase.find("a") + 1}')
print(f'A última letra "A" aparece na posição {phrase.rfind("a") + 1}')

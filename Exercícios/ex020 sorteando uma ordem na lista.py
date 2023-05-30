from random import shuffle

studentNames = []

for i in range(0, 4):
    names = str(input('Digite o nome do aluno(a): '))
    studentNames.append(names)

shuffle(studentNames)

print(f'A ordem de escolha de alunos para limpar a sala vai ser: \n{studentNames}')


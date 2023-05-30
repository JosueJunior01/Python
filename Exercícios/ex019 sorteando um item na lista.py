from random import choice
nomesDosAlunos = []
for i in range(0, 5):
    alunos = str(input('Nome do Aluno(a): '))
    nomesDosAlunos.append(alunos)
print(f'O aluno que vai limpar a sala vai ser {choice(nomesDosAlunos)}')

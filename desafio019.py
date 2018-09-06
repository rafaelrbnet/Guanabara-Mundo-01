# uM PROFESSOR QUER SORTEAR UM DE SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PORGRAMA QUE AJUDE ELE LENDO O NOME DELES E ESCREVA O NOME DO ESCOLHIDO

from random import choice

a1 = str(input('Qual o nome do aluno 1? '))
a2 = str(input('Qual o nome do aluno 2? '))
a3 = str(input('Qual o nome do aluno 3? '))
a4 = str(input('Qual o nome do aluno 4? '))

items = [a1, a2, a3, a4]
print('O aluno escolhido foi: {}'.format(choice(items)))
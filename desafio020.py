# o mesmo professor do desafio anterior quer sorter a ordem de apresentacao dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

a1 = str(input('Qual o nome do aluno 1? '))
a2 = str(input('Qual o nome do aluno 2? '))
a3 = str(input('Qual o nome do aluno 3? '))
a4 = str(input('Qual o nome do aluno 4? '))

items = [a1, a2, a3, a4]
shuffle(items)

print('O order de papresentação é  {}'.format(items))
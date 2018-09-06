"""
Crie um programa que leia um numero inteiro qualquer e exiba se ele é par ou impar
"""

n = int(input('Digite um número inteiro qualquer: '))
print('O número {} é {}'.format(n, 'PAR' if n % 2 == 0 else 'ÍMPAR'))
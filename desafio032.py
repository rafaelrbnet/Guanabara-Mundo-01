"""
faça um programa que leia um ano e mostes se ele é BISSEXTO

BISSEXTO =
- divisivel por 4
- nao divisivel por 100
- ou divisivel por 400
"""

from datetime import date
a = int(input('Digite um ano, ou  0 para analisar o nano atual:  '))

if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é Bisexto'.format(a))
else:
    print('O ano {} NÃO é Bisexto'.format(a))
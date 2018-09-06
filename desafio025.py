# Escreva um programa que leia um nome de uma pessoa e diga se ela tem SILVA no nome

n = str(input('Qual o seu nome completo: '))

if 'silva' in n.lower():
    print('O nome {} contem SILVA'.format(n))
else:
    print('O nome {} NÃO contem SILVA'.format(n))

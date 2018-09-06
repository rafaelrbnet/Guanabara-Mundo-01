# Crie um programa que leia no nome comoleto de uma pessoa e mostre

nome = str(input('Qual o seu nome cmpleto? ')).strip()

print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Quantas letras ao todo: {}'.format(len(nome)-nome.count(' ')))

primeiro = nome.split()
print('O primeiro nome  ({}) tem {} letras'.format(primeiro[0], len(primeiro[0])))


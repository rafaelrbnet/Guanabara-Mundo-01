# crie um programa que leia dois númerosw e mostre a soma entre eles
n1 = int(input('\033[1;30mQual o primeiro número?\033[m')) # negrito e branco
n2 = int(input('\033[47mQual o segundo número?\033[m')) # back cinza
s = n1 + n2

print('\033[33mA soma dos dos números é {}\033[m' .format(s)) # amarelo

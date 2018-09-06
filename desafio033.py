"""
FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR
"""

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

#assumindo que menor e maior é o n1
menor = n1
maior = n1

# verificando o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3

# verificando o maior
if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n1:
    maior = n3

print('O menor número é {} e o menor é {}'.format(menor, maior))

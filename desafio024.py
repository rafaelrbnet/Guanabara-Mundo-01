# Escfreva um programa que leia o nome de uma cidade e escreva se ela começa ou não com santo

c = str(input('Qual cidade você mora? ')).strip().lower()
separada = c.split()

if separada[0].find('santo') != -1:
    print('A cidade {} começa com Santo'.format(c))
else:
    print('A cidade {} não começa com santo'.format(c))

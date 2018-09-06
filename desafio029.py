"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar os 80km/h, mostre uma mensagem dizendo que ele foi muntado.
A multa vai custar R$7,00 para cada Km acima do limite
"""

v = float(input('Qual a velocidade de seu carro? '))

if v > 80:
    print('Você ultrapassou o limite de 80km/h e foi multado em R$ {:.2f}'.format((v-80)*7))
else:
    print('PARABÉNS, Vc está dentro do limite de velocidade.')

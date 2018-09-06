'''
Escreva um prograama que faça o computador pensar em um númeto inteiro entre 0 e 5 e peça para o usuário tentr
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário vencei ou perdeu.
'''

from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5')
print('-=-'*20)
sorteio = randint(1, 5)
escolhido = int(input('Digite o número que eu estou pensando! '))
print('Processando')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
print('ACERTOU' if sorteio == escolhido else 'ERROU eu pensei no {} kkk'.format(sorteio))

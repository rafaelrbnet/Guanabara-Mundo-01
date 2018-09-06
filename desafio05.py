# faça um programa que leia um número inteiro e mostre na tela o seu sucessor
# e seu antecessor

n = int(input('\033[34;43mDigite um número:\033[m'))

print('\033[47mO andecessor do número {} é {} e o sucessor é {}\033[m'.format(n, n-1, n+1))

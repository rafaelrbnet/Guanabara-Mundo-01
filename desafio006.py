# crie um algoritimo que leia um número e mostre o seu dobro, triplo e a raiz qudrada

n = int(input('\033[7mDigite um número\033[m'))

print('\033[7;36mO dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}\033[m'.format(n**2, n**3, n**(1/2)))

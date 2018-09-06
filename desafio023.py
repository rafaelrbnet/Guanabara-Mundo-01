# Faça um programa que leia um número de 0 a 9999e mostre na tela cada um dos dígitos separados
# so podemos fazer por mateatica, pois se o numero digitado for < que 4 digitos daria erro na hora de capturar o indice
# da lista de caracteres

n = int(input('Digite um número de 1 a 9999: '))

u = n // 1 % 10 # divisão inteira por 1 (Unidade) e depois pegar o resto da dovisão por 10
d = n // 10 % 10 # divisão inteira por 10 (Dezena) e depois pegar o resto da dovisão por 10
c = n // 100 % 10 # divisão inteira por 100 (Centena) e depois pegar o resto da dovisão por 10
m = n // 1000 % 10 # divisão inteira por 1000 (Milhar) e depois pegar o resto da dovisão por 10

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
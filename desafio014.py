# escreva um programa que converta uma temperatura digitada em °C e converta em °F
c = float(input('Digite a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC  covertida é  {}ºF'.format(c, f))
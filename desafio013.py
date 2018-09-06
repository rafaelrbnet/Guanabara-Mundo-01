# escreva um programa que leia o salário de um funcionário e mostre o salário com 15% de aumento

s = float(input('Qual o seu salário? R$'))
a = s + (s * 15/ 100)
print('Seu salário de R${:.2f} com 15% de aumento é de R${:.2f}'.format(s, a))
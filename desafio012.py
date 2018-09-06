# faça um programa que leia o preço  de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Qual o preço dp produto? R$'))
d = p - (p * 5 / 100)
print('O preço do seu produto que custava {:.2f} com 5% de desconto é R$ {:.2f}'.format(p,d))
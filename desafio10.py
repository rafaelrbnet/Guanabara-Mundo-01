10# crie um programa que leia quanto dinehiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# considere US$ 1,00 = R$ 3,27

d = float(input('Quanto de dinheiro vc tem na carteira? R$'))
u = 3.27
print('Com o dólar cotado a R${:.2f} você pode comprar US${:.2f} '.format(u,d/u))
# faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta
# necessária para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Qual a largura da parede em metros?'))
a = float(input('Qual a altura  da parede em metros?'))

area = l*a

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m² A quantidade de tinta necessária para pintar é de {} litros'.format(l, a, area,(area/2)))
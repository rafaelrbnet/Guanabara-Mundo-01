"""
Escreva um programa que pergune o salário de um funcionário e calcule o valor do seu aumneto.
Para salários superiores a R$ 1.25o,00 calcule um aumento de 10%
para os inferiores ou iguais, o aumento é de 15%
"""

s = float(input('Qual o seu salário atual?'))

# modo simplicifaco print('Com base em seu salário atual o seu aumento será de {}% e seu novo salário será de {} PARABÉNS!'.format('10' if s > 1250 else '15', s+(s*0.10) if s > 1250 else s+(s*0.15)))

if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, novo))

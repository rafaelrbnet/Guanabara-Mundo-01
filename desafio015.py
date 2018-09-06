# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

km = float(input('Qual a quantidade de Km percorridos?'))
dias = int(input('Quantos dias você rodou com ele?'))

p_km = km * 0.15
p_dias = dias * 60

print('O valor a pagar pelos {}km rodados é R${:.2f}\nValor a pagar pelos {} dias de aluguel é R${:.2f}\n{}\nTotal R${:.2f}'.format(km, p_km, dias, p_dias, 30*'-', p_km+p_dias))
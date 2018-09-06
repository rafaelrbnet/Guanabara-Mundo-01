# operadores lógicos
print (5 + 2) # adição
print (5 - 2) # subtração
print (5 * 2) # multiplicação
print (5 / 2) # Divisão
print(5 ** 2) # Potência
print(5 // 2) # Divisão Inteira
print(5 % 2) # Resto da divisão

# ordem da procedencia (qual função matemátca execta primeiro)
# 1 ()
# 2 **
# 3 * / ** //
# 4 + -

print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

# brincando com strings
nome = input('Qual o sseu nome?')

print('Meu nome é {:20}!'.format(nome)) # setando a quantidade de caracteres para a mascara
print('Meu nome é {:>20}!'.format(nome)) # setando a quantidade de caracteres para a mascara alinhado a direita
print('Meu nome é {:<20}!'.format(nome)) # setando a quantidade de caracteres para a mascara alinhado a esquerda
print('Meu nome é {:^20}!'.format(nome)) # setando a quantidade de caracteres para a mascara alinhado a centro
print('Meu nome é {:=^20}!'.format(nome)) # setando a quantidade de caracteres para a mascara alinhado a centro

# dormatação de números
n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto  é {}, e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira é {}\n e potência {} '.format(di, e))
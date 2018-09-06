# CONDIÇÕES
# PYTHON USA IDENTAÇÃO E : PARA DELIMITAR AS CONDIÇÕES
'''

tempo = int(input('Qauntos anos tem seu carro? '))
if tempo<=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('---Fim---')
'''

# CONDIÇÃO SIMPLES É QUAN EM SO O IF() TRUE

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))

# CONDIÇÃO COMPOSTA
'''
if m>=6:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
'''

# CONDIÇÃO SIMPLIFICADA
# PYTHON NÃO POSSUI OPERADOR TERNARIO
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS')

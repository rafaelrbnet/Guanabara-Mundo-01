"""
DESENVOLV UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO r$ 0,50 POR
KM PARA VIAGENS ATÉ 200KM E r$ 0,45 PARA VIAGENS MAIS LONGAS
"""

d = float(input('Qual a distância da viagem em km? '))
print('Tarifa por km é R$ {} e o preço desta viagem é R$ {:.2f}'.format('0,50' if d <= 200 else '0,45', d*0.50 if d <= 200 else d*0.45))

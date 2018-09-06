"""
DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUARIO SE ELAS PODEM OU NÃO FAZER UM TRIÂNGULO

Sabemos que um triângulo é formado por três lados que possuem uma determinada medida, mas essas não podem ser escolhidas
aleatoriamente como os lados de um quadrado ou de um retângulo, é preciso seguir uma regra.

Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior
que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados. Veja o resumo
da regra abaixo:

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

"""
a = float(input('digite o tamanho em cm da lateral A do triângulo: '))
b = float(input('digite o tamanho em cm da lateral B do triângulo: '))
c = float(input('digite o tamanho em cm da lateral C do triângulo: '))

ta = (b - c) < a < b + c
tb = (a - c) < b < a + c
tc = (a - b) < c < a + b

print('As medidas informadas {} formar um triângulo'.format('PODEM' if ta and tb and tc else 'NÃO PODEM'))

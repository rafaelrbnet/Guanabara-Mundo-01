#faça um programa que leia algo pelo teclado e mostre na tela
# # o seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('\033[4;36;43mDigite algo: \033[m');

tipo = type(algo)
ealpha = algo.isalpha()
enumeric = algo.isnumeric()
eupper = algo.isupper()

print('\033[30mA variável {} digitada é do tipo: {}\033[m' .format(algo, tipo))
print('\033[31mA variável {} digitada é alphanumérica?  {}\033[m' .format(algo, ealpha))
print('\033[32mA variável {} digitada é numérica? {}\033[m' .format(algo, enumeric))
print('\033[33mA variável {} digitada está em maiúscula? {}\033[m' .format(algo, eupper))

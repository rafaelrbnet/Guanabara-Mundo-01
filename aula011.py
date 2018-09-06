# Cores no termial
'''
ANSI escape sequence
padrão cor
\033[
estilo;
texto;
fundo
m

texto

\033[m
consulte as cores em aula011.PNG


pesquisar o colorize
'''

print('\033[7;33;44mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'rafael'
print('Olá {}{}{} !!!'.format('\033[4;34m',nome,'\033[m'))

# usando listas
cores = {'limpa' :' \033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7:30m'}

print('Olá {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))

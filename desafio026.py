# faça um programa que leia uma frase pelo teclado e mostre:

frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))



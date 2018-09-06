#    caracteres

frase = '  Curso em Vídeo Python  '
print(frase[3]) # so do o 3
print(frase[3:10]) # do 3 ate o 10(10 nao entra)
print(frase[::2]) #Do começo ao final de 2 em 2

print("""Agora
tem um monte
de texto""")

print(frase.count('o')) # conta os caracteres
print(len(frase)) # conta tamanho

print(frase.strip()) # tira os espaços
print(frase.rstrip()) # tira os espaços da esquerda

print(frase.replace('Python','Android')) # tira os espaços

print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower())
print(frase.title().strip())
dividido = frase.split()
print(dividido )
print(dividido[0])
print('-'.join(dividido))

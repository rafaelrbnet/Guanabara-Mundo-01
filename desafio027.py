# escreva um programa que leia o noem completo de uma pessoa, mostrando o primeiro e o último nome separadamente

separado = str(input('Digite seu nome completo: ')).strip().split()


print('O primeiro nome é {} e o último é {}'.format(separado[0], separado[len(separado)-1]))

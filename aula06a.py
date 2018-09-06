n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
#formato antigo
# print('A soma de ',n1,' e ',n2, 'é {}'.format(s) )

#formato novo python3
print ('a soma entre {} e {} vale {}'.format(n1, n2, s))
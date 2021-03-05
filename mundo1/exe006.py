'''Criar um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada'''

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O dobro de {} é {}, \nseu triplo é {} \ne sua raiz quadrada é {:.2f}.'.format(n, d, t, rq))

# ou

print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(n, (n*2), (n*3), (n**(1/2))))

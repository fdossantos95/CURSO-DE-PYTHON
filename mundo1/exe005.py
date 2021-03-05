'''Criar um programa que leia um número e mostre na tela qual é o seu antecessor  e sucessor.'''

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O antecessor de {} é {} e seu sucessor é {}.'.format(n, a, s))

# ou

print('O antecessor de {} é {} e seu sucessor é {}.'.format(n, (n-1), (n+1)))

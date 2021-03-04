'''Como funcionam os tipos primitivos e as peculiaridades do int(), float(), bool() e str()

4 Tipos Primitivos básicos (int, float, bool, str)

Quando a variavel recebe um número apenas utilizando o input o Python realiza a concatenação e não a operação aritmética desejada, porque o número é apenas uma mensagem sem a designação do tipo promitivo:
ex: n1 = input('Digite um número: )

Tipo primitivo int (inteiro)

Ao adicionarmos o tipo primitivo int, tudo o que estiver dentro do parenteses será convertido para um número inteiro, veja:'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é {}.'.format(n1, n2, s))

# Antes:
n1 = input('Digite um valor: ')
print(type(n1))

# Depois
n1 = int(input('Digite um número: '))
print(type(n1))

'''Tipo primitivo float'''

n = float(input('Digite um número: '))
print(n)

'''Tipo primitivo str'''
n = str(input('Digite um número: '))
print(n)

'''Tipo primitivo bool, mostra se é verdadeiro ou falso'''
n = bool(input('Digite um número: '))

'''Outros exemplos:'''

n = input('Digite algo: ')
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isupper())

# etc.
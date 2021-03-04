'''Comandos básicos em Python

A primeira coisa a se entender em Python é que, se os dados forem uma mensagem eles tem delimitadores especiais, exemplo:
'' as aspas, simples ou duplas.
 
Para o Python, todos os comandos são funções e todas as funções tem que ter parenteses:
() parentes podem ser usados com qualquer função.
  
print = escreva, serve para você pedir que o Python escreva uma mensagem na tela:'''

print('Olá mundo!')

''' Nem todas as mensagens estarão entre aspas, por exemplo os números:'''
print(7+4)

# ou para juntar um número a outro:
print('7'+'4')

'''Tem horas que o sinal de + vai funcionar melhor e tem horas que a vírgula vai funcionar melhor:
print('Olá' + 5) # neste caso dará um erro'''

# aí então usamos vírgula:
print('Olá' , 5)

###########################################################################################################

'''Utilização de Variáveis:

Como exemplo, se quisermos registrar o nome, peso e a idade de uma pessoa?
Toda variável é um objeto para o Python, e pode receber valores, e o 'recebe' é representado pelo simbolo de igual ='''

nome = 'Fabiano'
peso = 95.5
idade = 35
print(nome, peso, idade)

'''Utilizando a função 'input', que significa 'leia':'''
nome = input('Qual é seu nome? ')
peso = input('Quanto você pesa? ')
idade = input('Qual é a sua idade? ')
print('Seu nome é {}, você pesa {}kg e tem {} anos.'.format(nome, peso, idade))

# Desafio número 1: Criar um script que leia o nome de uma pessoa e mostre uma mensagem de boas vindas:

nome = input('Qual é seu nome? ')
print('Seja bem vindo {}!!!'.format(nome))

# Desafio número 2: Criar um script que leia dia, mês e ano de nascimento e mostre uma mensagem com a data formatada:

dia = input('Em que dia você nasceu? ')
mes = input('Qual o mês do seu nascimento? ')
ano = input('Em que ano você nasceu? ')
print('Sua data de nascimento é {}/{}/{}.'.format(dia, mes, ano))

# Desafio número 3: Criar um script que leia dois números e mostre a soma entre eles:

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print('A soma entre {} e {} é {}.'.format(num1, num2, soma))

# Neste desafio foi utilizado o tipo primitivo 'int' que será ensinado na proxima aula.

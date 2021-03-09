'''Criar um algoritmo que leia o salario de um funcionário e mostre seu novo salario, com 15% de almento.'''

print('-'*60)
salario = float(input('Digite seu salário atual: R$ '))
aumento = (salario * (15/100)) + salario
print('Seu salário atual é R${:.2f}, mas com 15% de aumento você passa a receber R${:.2f}.'.format(salario, aumento))
print('-'*60)

'''Criar um programa que leia o preço de um produto e aplique 5% de desconto, mostrando seu novo preço.'''

print('$'*65)
preço = float(input('Qual o preço do produto: R$ '))
npreço = preço - ((5/100) * preço)
print('Este produto com 5% de desconto sai de R${} por R${}.'.format(preço, npreço))
print('$'*65)

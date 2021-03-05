'''Criar um programa que converta real em dolar.'''

print('-'*50)
real = float(input('Quantos reais você para converter em dolar? R$ '))
cotação = real / 5.17
print('Com R${:.2f} é possível comprar U${:.2f}.'.format(real, cotação))
print('-'*50)

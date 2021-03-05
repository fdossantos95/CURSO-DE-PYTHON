'''Criar um programa que leia a altura e a largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma area de até 2 metros quadrados.'''

print('->'*60)
a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
area = l * a 
tinta = area / 2
print('Para uma parede de {} metros de altura e {} metros de largura serão necessários {:.2f} litros de tinta, considerando-se uma area de {}m².'.format(a, l, tinta, area))
print('->'*60)

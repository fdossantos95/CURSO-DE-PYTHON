'''A utilização de módulos.'''

# import
# Ex:

from math import sqrt

#para importar algo da bibilioteca Math.

# ceil: arredondamento para cima
# floor: arredondamento para baixo
# trunc: elimina da virgula para frente, sem fazer arredondamentos
# pow: potenciação
# sqrt: raiz quadrada
# factorial: fatorial de uma numero

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num, raiz))

import random
num = random.random()
print(num)

# ou

num = random.randint(1, 10)
print(num)

import emoji
print{emoji.emojize("Olá mundo! :sunglasses:", use_aliases=True)}


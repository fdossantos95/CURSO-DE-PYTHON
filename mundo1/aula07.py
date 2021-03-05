''' Operadores Aritméticos 

+  Soma
-  Subtração
*  Multiplicação
/  Divisão
** Potência (ou pow())
// Divisão inteira
%  Resto da divisão

Ordem de precedência

1º ()
2º **
3º *, /, //, %
4º +, -'''

''' {:20} escreve em um intervalo de 20 espaços
    {:>20} alinhado a direita
    {:<20} alinhado a esquerda
    {:^20} centralizar
    {:=^20} centralizado e preenchendo os vazios com sinal de igual'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}.'.format(n1+n2))

# ou

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print('A soma vale {}, \na subtração {}, \no produto {}, \na divisão {:.2f}, \na potenciação {}, \na divisão inteira {} e \no resto da divisão vale {}.'.format(s, sb, m, d, p, di, r))

# {:.2f} determina o número de casas após a virgula
# end='' , impede a quebra de linha
# \n , quebra de linha

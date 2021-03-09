'''Programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelo qual ele foi alugado. Calcule o preço a pagar sabendo que o carro custa $60,00/dia e $0,15/km.'''

print('-'*60)
km = int(input('Quantos kilometros foram percorridos? '))
dias = int(input('Por quantos dias você alugou o carro? '))
valor = (dias * 60) + (km * 0.15)
print('-'*60)
print('O valor total a ser pago pelo aluguel do veículo é R${}.'.format(valor))
print('-'*60)

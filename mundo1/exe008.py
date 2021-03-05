'''Criar um programa que leia um valor em metros e faça a conversão para centímetros e milímetros.'''

m = float(input('Digite a medida em metros: '))
c = m * 100
mm = m * 1000
print('{:.0f} metros é equivalente a {:.0f} centímetros e a {:.0f} milímetros.'.format(m, c, mm))

# ou

print('{} metros é equivalente a \n{} centímetros e a \n{} milímetros.'.format(m, (m*100), (m*1000)))

#faça um programa que leia os lados de um triangulo retangulo e mostre o comprimento da hipotenusa
import math
print('***** calculo de triangulo retangulo *****')
ca=float(input('digite o valor do cateto adjacente'))
co=float(input('digite o valor do cateto oposto'))
h=ca**2+co**2
h=h**(1/2)
# o comando math.hypot(ca, co) calcula a hipotenusa se der o valor dos catetos.
print('o valor da hipotenusa é {:.2f}'.format(h))

#faça um programa que sorteie uma pessoa dentre 4
import random
g = str('gustavo')
l = str('lucas')
m = str('maria')
j = str('jose')
lista = [g, l, m, j]
escolido = random.choice(lista)
print('O nome da pessoa escolhida é: {}'.format(escolido))

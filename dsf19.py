#um progama que escolha 4 nomes ou numeros, embaralhe e apresente uma ordem aleatoria.
import random
n1 = input('escreva o primeiro nome:')
n2 = input('escreva o segundo nome:')
n3 = input('escreva o terceiro nome:')
n4 = input('escreva o quarto nome:')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem apresentada foi:\n {}'.format(lista))

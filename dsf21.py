#programa que peça o nome completo de uma pessoa e exiba os seguintes resultados:
#nome com todas as letras maiusculas;
#nome com todas as letras minusculas;
#quantas letras tem no total(sem contar espaços);
#quantas letras tem o primeiro nome;
nome = str(input('digite seu nome completo:')).strip()
lista = nome.split()
print('Seu nome com todas as letras maiusculas fica assim:\n{}'.format(nome.upper()))
print('e com as letras minusculas fica assim:\n{}'.format(nome.lower()))
print('Seu nome tem {} letras no total!'.format(len(nome) - nome.count(' ')))
print('e seu primeiro nome tem {} letras.'.format(len(lista[0])))

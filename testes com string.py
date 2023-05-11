#algumas funçoes para fatiamento de string
nome = 'Lucas de Jesus Vasconcelos'
print(nome[6])#vai mostrar o 6º espaço da string.
print(nome[6:14])#vai mostrar do espaço 6 até o espaço 13 na sting.
print(nome[:14])#vai mostrar do começo até o espaço 13 da string.
print(nome[14:])#vai mostrar do espaço 13 até o final da string.
print(nome[0:14:2])#vai mostrar do espaço 0 até o espaço 13 pulando um caractere.
print(nome[0:14:3])#vai mostrar do espaço 0 até o espaço 13 mostrando a cada 2 caracteres.
print("""PUDIM
1 lata de leite condensado
1 lata de leite (medida da lata de leite condensado)
3 ovos inteiros
CALDA
1 xícara (chá) de açúcar
1/2 xícara de água""")
#utilizando o comando print(""" """)com 3 aspas duplas(") eu posso digitar livremente no codigo;
#que vai exibir no programa da maneira que eu digitei no script.
print(nome.count('s'))#vai mostar quantos 's' tem na string(note que vai considerar apenas s minusculo.)
print(nome.upper())#deixa toda minha string em letras maiusculas.
print(nome.lower())#deixa toda minha string em letras minusculas.
print(len(nome))#vai mostrar a quantidades de caracteres na string.
nome2= '   Lucas de Jesus Vasconcelos   '
print(nome2.strip())#strip() serve para remover os espaços em branco no inicio e no final da string.
print(nome.replace('Vasconcelos', 'Pudim'))#replace serve para alterar o conteúdo da string (no caso troquei o nome;
#Vasconcelos para Pudim.
print('Lucas' in nome)#'Lucas' está na variavel nome?
print(nome.find('Jesus'))#'Jesus' está em qual posição?
lista = nome.split()#split() cria uma lista separando os nomes da string separados por espaço.
print(lista)
print(lista[2])#mostra o 3º nome da lista.

#faça um programa que leia uma frase e diga, quantas vezes a letra 'a' aparece, quando ela aparece;
#pela primeira vez e quando ela aparece na ultima vez.
frase = input('digite uma frase')
frase = frase.lower()
print('quantidade de letras "a" na sua frase:')
print(frase.count('a'))
print('a letra "a" é aparece primeiro no espaço:')
print(frase.find('a'))

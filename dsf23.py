#faça um programa pra pessoa digitar o nome de sua cidade e falar se começa com a palavra 'Santo'
c = input('qual o nome da sua cidade?')
c = c.upper()
c = c.split()
print('sua cidade começa com o nome "santo"?')
print('SANTO' in c[0])

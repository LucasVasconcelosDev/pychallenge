#pegar o valor de algo e dar o desconto de 5%
p=float(input('qual o preço deste produto?'))
d=p*5/100
np=p-d
print('o novo preço com 5% de desconto é {}R$'.format(np))

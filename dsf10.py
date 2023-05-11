#calcular a area da parede e mostrar quanto?s baldes de tinta precisa para pintar
h=float(input('quantos metros tem sua parede?'))
b=float(input('qual a largura da sua parede?'))
p=b*h
qn= int(p/2)
print('considerando que cada balde de tinta pinta 2metros quadrados, vc precisa de\n {} baldes para pintar tudo.'.format(qn))

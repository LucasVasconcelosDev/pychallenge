n1=int(input('digite o primeiro número numero:'))
n2=int(input('digite o segundo número numero:'))
s=n1+n2
d=n1-n2
m=n1*n2
ex=n1**n2
r1=n1**(1/2)
r2=n2**(1/2)
d=n1/n2
dr=n1//n2
r=n1%n2
print('{} + {} = {}'.format(n1, n2, s))
print('{} - {} = {:.2f}'.format(n1, n2, d))
print('{} x {} = {}'.format(n1, n2, m))
print('({})^{}={}'.format(n1, n2, ex))
print('raiz de {} ={:.2f}'.format(n1, r1))
print('raiz de {}={:.2f}'.format(n2, r2))
print('{}/{}={:.2f} (arredondado para {} e com o resto da divisão sendo{})'.format(n1, n2, d, dr, r))

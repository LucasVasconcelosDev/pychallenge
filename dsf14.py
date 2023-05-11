#este programa deve perguntar e calcular quantos dias e km foram percorridos por um carro alugado.
#cada dia de aluguel custa R$60 e cada km rodado custa R$0,15.
dias=int(input('este carro foi alugado durante quantos dias?'))
dias=dias*60
km=float(input('quantos KM foram percorridos neste tempo?'))
km=km*0.15
p=dias+km
print('considerando os valores, o preço total é de R${:.2f}'.format(p))

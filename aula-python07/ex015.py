dias = int(input("Digite quantos km do carro alugou  "))
kilo = float(input("Quantos kilometros percorreu "))
aluguel = dias * 60
km = kilo * 0.15
preco = (aluguel + km)
print("Com {} dias o valor usou em km {} a pagar é {}".format(dias,aluguel,preco))
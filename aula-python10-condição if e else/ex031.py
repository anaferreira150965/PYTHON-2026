distancia = float(input("Qual a distancia da sua viagem "))

if distancia <= 200:
    preco1 = distancia * 0.50
    print(f"O preço da sua viagem foi R$ {preco1:.2f} ")
else:
    preco2 = distancia * 0.45
    print(f"O preço da sua viagem foi R$ {preco2:.2f}")
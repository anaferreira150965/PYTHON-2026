velocidade = float(input("Digite a velocidade do carro : "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Voce ultrapassou a velocidade de {velocidade}" )
    print(f"O valor da multa é R$ {multa:.2f}")
else:
    print("Você está dentro da velocidade")
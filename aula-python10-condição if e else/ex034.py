salario = int(input("Digite o seu salário : "))
if salario <= 1250:
    novo = (salario * 15 / 100)

    print(f'O seu aumento foi de 15% R$ {salario + novo:.2f}')
else:
    novo = (salario * 10 / 100)
    print(f'O seu aumento foi de 10% R$ {salario + novo:.2f}')



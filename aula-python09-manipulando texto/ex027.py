nome = str(input("Digite seu nome : ")).strip()

separa = nome.split()

print("O primeiro nome é {} ".format(separa[0]))
print("O seu ultimo nome é {} ".format(separa[-1]))
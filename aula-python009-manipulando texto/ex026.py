frase = str(input("Digite uma frase : ")).strip().upper()

print("A letra A aperece {} vezes".format(frase.count("A")))
print("A letra primeira letra A aperece na posição {} ".format(frase.find("A") + 1))
print("A ultima letra A aparece na posição {} ".format(frase.rfind("A") + 1))



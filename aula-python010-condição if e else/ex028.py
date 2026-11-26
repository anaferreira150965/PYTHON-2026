import random

num = int(input("Pense em um numero de 0 a 05 ... "))
n = random.randint(0,5)
if num == n :
    print(f"Pensei no numero {n} Voce acertou")
else:
    print(f"Pensei no numero {n} Voce errou")

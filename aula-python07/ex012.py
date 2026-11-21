num = float(input("Qual o preço do produto : "))
desc = (num * 5 / 100)
tot = num - desc
print("O produto custa R$ {:.2f} e com o desconto de R$ {:.2f} custará R$ {:.2f}".format(num,desc, tot))
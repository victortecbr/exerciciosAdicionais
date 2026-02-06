#peça tres números e mostre o maior valor.
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))
if num1 >= num2 and num1 >= num3:
    print("Maior número", num1)
elif num2 >= num1 and num2 >= num3:
    print("Maior número", num2)
else :
    print("Maior número", num3)

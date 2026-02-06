#Peça dois numeros e mostre o maior.
num1 = float(input("Digite primeiro número:"))
num2 = float(input("Digite segundo número:"))
if num1 > num2: print(f"numero maior", num1)
elif num2 > num1: print(f"numero maior", num2)
else: print(f"numeros iguais")
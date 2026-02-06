# 14.Solicite 5 números do usuário e mostre:
# quantos são pares
# quantos são ímpares

print("Digite 5 numeros e veja quais são pares e quis são impares.")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
num4 = int(input("Número 4: "))
num5 = int(input("Número 5: "))

if num1 % 2 == 0:
    print(f"{num1} é par")
else:
    print(f"{num1} é ímpar")

if num2 % 2 == 0:
    print(f"{num2} é par")
else:
    print(f"{num2} é ímpar")

if num3 % 2 == 0:
    print(f"{num3} é par")
else:
    print(f"{num3} é ímpar")

if num4 % 2 == 0:
    print(f"{num4} é par")
else:
    print(f"{num4} é ímpar")

if num5 % 2 == 0:
    print(f"{num5} é par")
else:
    print(f"{num5} é ímpar")
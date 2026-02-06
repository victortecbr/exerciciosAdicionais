#Peça um número e verifique se está entre 10 e 50.
num = int(input("Digite um numero: "))
if  10 <= num <= 50:
    print(f"dentro do intervalo.{num}")
else:
    print(f"fora do intervalo.{num}")
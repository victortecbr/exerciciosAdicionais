#Peça ao usuário um número e diga se 
# ele é divisivel por 3 e 5 ao mesmo tempo.
num = int(input("Digite um número: "))
if num % 3 == 0 and num % 5 == 0:
    print("É divisivel por 3 e 5.")
else:
    print("Não é divisivel por 3 e 5.")

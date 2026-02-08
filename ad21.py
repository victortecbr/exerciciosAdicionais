#Função para IMC

def calcular_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = calcular_imc(peso, altura)
print(imc)


#situação do imc

if imc < 18.5:
    print("Baixo Peso")
elif imc < 24.9:
    print("Peso Normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesidade Grau I")
elif imc < 39.9:
    print("Obesidade Grau II (Severa)")
else:
    print("Obesidade Grau III (Mórbida)")
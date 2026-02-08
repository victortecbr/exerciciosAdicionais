# Exercício 1 – Controle de Consumo de Combustível

# Enunciado
# Crie um programa em Python que ajude um motorista a calcular o consumo médio do carro.
# Regras
# Crie uma função chamada calcular_consumo

# A função deve receber:
# quilômetros rodados
# litros de combustível gastos
# A função deve retornar o consumo médio (km por litro)

# Programa principal
# Leia os valores do usuário
# Chame a função
# Mostre o consumo com a mensagem:

def calcular_consumo(km, litros):
    return km / litros

km = float(input("Digite a quantidade de (Km) rodado: "))
litros = float(input("Digite litros o combustível usado: "))

consumo_medio = calcular_consumo(km, litros)
print(f"Você rodou {km} e consumiu {litros}")
print(f"Seu consumo médio é {consumo_medio}km/litro")
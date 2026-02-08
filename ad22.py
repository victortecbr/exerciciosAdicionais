# Crie funções para:

# soma
# subtração
# multiplicação
# divisão

# Leia dois números e mostre todos os resultados.

def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b != 0:
        return a / b
    else:
        return "divisão inválida por zero: "

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resu_soma = soma(n1, n2)
resu_sub = sub(n1, n2)
resu_mult = mult(n1, n2)
resu_div = div(n1, n2)

print(f"{resu_soma} Resultado da soma")
print(f"{resu_sub} Resultado da subtração")
print(f"{resu_mult} Resultado da multiplicação")
print(f"{resu_div} Resultado da divisão")
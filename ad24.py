# Crie funções para:

# INSS
# Vale transporte
# Bônus
# Cargo

# No final, mostre:

# Nome
# Salário bruto
# Descontos
# Bônus
# Salário líquido
# Cargo

def calc_inss(salario):
    if salario <= 1621.00:
        return salario * 0.075
    elif salario <= 2902.84:
        return salario * 0.09
    elif salario <= 4354.27:
        return salario * 0.12
    else:
        return salario * 0.14
    
def calc_vale(salario):
    if salario <= 1500.00:
        return 90.00
    elif salario <= 2000:
        return 120
    elif salario <= 3000:
        return 180
    else:
        return 240
    
def calc_bonus(salario):
    if salario <= 1000:
        return 100
    elif salario <= 2000:
        return 200
    elif salario <= 3000:
        return 300
    else:
        return 400
    
def calc_cargo(salario):
    if salario <= 1500:
        return "Auxiliar"
    elif salario <= 2000:
        return "Assistente"
    elif salario <= 3000:
        return "Técnico"
    elif salario <= 6000:
        return "Encarregado"
    else:
        return "Coordenador"

def calc_liq(salario,vale,inss,bonus):
    return salario - vale - inss + bonus

nome = input("Digite o nome: ")
salario = float(input("Digite o salário R$"))

inss = calc_inss(salario)
vale = calc_vale(salario)
bonus = calc_bonus(salario)
cargo = calc_cargo(salario)
liquido = calc_liq(salario,vale,inss,bonus)


print(f"Desconto INSS: R${inss}")
print(f"Desconto Vale: R${vale}")
print(f"Bônus: R${bonus}")
print(f"Salário líquido: R${liquido}")
print(f"cargo de trabalho: {cargo}")
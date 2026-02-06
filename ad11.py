# 11. Crie uma calculadora usando match-case:
# entrada: dois números + operador (+, -, *, /)
#(match-case)

print("-- Calculadora Básica (soma, subtrai, multiplica e divide) --")
num1 = float(input("Digite 1°: "))
ope = input("(+)(-)(*)(/): ")
num2 = float(input("Digite °: "))

match ope:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print(f"Número inválido")

# 19.Crie um menu interativo com while:
# 1 – Verificar par ou ímpar
# 2 – Calcular média de notas
# 3 – Mostrar tabuada
# 0 – Sair

print("\nescolha uma opção:")
print("1 – Verificar par ou ímpar")
print("2 – Calcular média de notas")
print("3 – Mostrar tabuada")
print("0 – Sair")

op = int(input("\nDigite a opção escolhida: "))

while op != 0:
    match op:
        case 1:
            int(iput("Digite o número: "))
            if op % 2 == 0:
                print("par")
            else:
                print("ímpar")
        case 2:
            qnt = 1
            while nota != "m":
            nota = float(f"Digite a {qnt} nota, digite "m" para obter a média.")
            nota += nota
                


    

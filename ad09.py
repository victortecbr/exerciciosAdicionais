# 9.	Solicite um número de 1 a 7 e mostre o dia da semana.
# (match-case)

print("-- Dias da semana --")
num = int(input("Digite um número de 1 a 7: "))

match num:
    case 1:
        print("dom")
    case 2:
        print("seg")
    case 3:
        print("ter")
    case 4:
        print("qua")
    case 5:
        print("qui")
    case 6:
        print("sex")
    case 7:
        print("sab")
    case _:
        print("Número inválido")


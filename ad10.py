# 10.	Solicite um número de 1 a 12 e mostre o mês correspondente.
#(match-case)

print("-- Meses do ano --")
num =  int(input("Digite de 1 a 12: "))

match num:
    case 1:
        print("jan")
    case 2:
        print("fev")
    case 3:
        print("mar")
    case 4:
        print("abr")
    case 5:
        print("mai")
    case 6:
        print("jun")
    case 7:
        print("jul")
    case 8:
        print("ago")
    case 9:
        print("set")
    case 10:
        print("out")
    case 11:
        print("nov")
    case 12:
        print("dec")
    case _:
        print("Entrada inválida")
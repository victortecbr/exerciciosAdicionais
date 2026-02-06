# 12. Receba uma letra de conceito (A, B, C, D ou F) e exiba a avaliação correspondente.
# A → Excelente
# B → Bom
# C → Regular
# D → Ruim
# F → Reprovado
# Caso o usuário digite um valor diferente dos informados, exiba a mensagem “Conceito inválido”.
# #(match-case)

print("-- A→ Excelente, B→ Bom, C→ Regular, D→ Ruim, F→ Reprovado --")
opcao = input("Digite a avaliação: ").upper()

match opcao:
    case "A":
        print("Excelente")
    case "B":
        print("Bom")
    case "C":
        print("Regular")
    case "D":
        print("Ruim")
    case "E":
        print("Reprovado")
    case _:
        print("Conceito inválido")
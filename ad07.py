# 7.Leia a nota final de um aluno e mostre:
# Aprovado (≥7)
# Recuperação (≥5 e <7)
# Reprovado (<5)
#(if / elif / else)

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
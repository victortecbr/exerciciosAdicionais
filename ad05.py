# 5.Leia a idade do usuário e informe:
# o	menor de idade
# o	adulto >= 18
# o	idoso (≥ 60)
#(if / elif / else)

print("-- Descubra se você é Idoso, Adulto ou Criança --")

idade = int(input("Digite a sua idade: "))

if idade >= 60:
    print("Idoso")
elif idade >= 18:
    print("Adulto")
else:
    print("Criança")
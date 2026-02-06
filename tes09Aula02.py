#Leia duas notas e informe se o aluno foi 
# aprovado (media >=7), 
# em recuperação (>=5) ou reprovado.
not1 = float(input("Digite a primeira nota: "))
not2 = float(input("Digite a segunda nota: "))
media = (not1 + not2) / 2

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado.")
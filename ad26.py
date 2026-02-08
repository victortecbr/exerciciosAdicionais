# Crie um programa que verifique a situação de um aluno com base na média final.

# Regras
# Crie uma função chamada verificar_situaca

# A função deve receber:
# nota 1
# nota 2
# A função deve: calcular a média

# retornar:
# "Aprovado" se média ≥ 7
# "Recuperação" se média ≥ 5 e < 7
# "Reprovado" se média < 5

# Programa principal
# Leia as duas notas
# Chame a função

def calcular_media(nota1, nota2):
        return (nota1 + nota2) / 2

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

if n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10:
    print("Nota inválida")
else:
    media = calcular_media(n1, n2)
    classificacao = situacao(media)
    
    print(f"1° nota: {n1}")
    print(f"2° nota: {n2}")
    print(f"Média: {media}")
    print(f"Situação: {classificacao}")


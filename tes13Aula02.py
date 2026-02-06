#O usuário entra com o nome e valor de provas: prova 01,
# prova 02, prova 03. O algoritmo mostra no final as 
# informações inseridas pelo usuário e a média 
# calculada entre eles:

nome = input("Digite o nome do aluno:")
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

print(f"\n--- Boletin do aluno: ---")
print(f"Nome do aluno: {nome}")
print(f"Nota 1: {nota1}")
print(f"Nota 1: {nota2}")
print(f"Nota 1: {nota3}")
print(f"Média final: {media}")
print(f"\n--- Fim do Boletin do aluno: ---")

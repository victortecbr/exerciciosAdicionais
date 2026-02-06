# 16.Peça números ao usuário até que ele digite 0. Ao final, mostre:
# soma total
# média
#(while)

soma = 0
quantidade = 0

numero = float(input("Digite um número (0 para sair): "))

while numero != 0:
    soma += numero
    quantidade += 1
    numero = float(input("Digite um número (0 para sair): "))

if quantidade > 0:
    media = soma / quantidade
    print("Soma total:", soma)
    print("Média:", media)
else:
    print("Nenhum número foi digitado.")

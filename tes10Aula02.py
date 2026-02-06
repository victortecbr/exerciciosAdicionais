#peça ao usuário o valor de uma compra e 
# informe se ele ganha desconto de 10% (valor > 100).
valor = float(input("Digite o valor da sua compra: "))
if valor > 100:
    valor = valor * 0.9
    print(f"Desconto aplicado! Total: R${valor}")
else:
    print(f"sem desconto! Total: R${valor}")
    
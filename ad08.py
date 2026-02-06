# 8.Solicite o salário bruto e informe:
# valor do INSS
# valor do vale transporte
# salário líquido
# (use regras semelhantes às da apostila, mas organize melhor as variáveis)

#INSS
#Até R$ 1.621,00: 7,5%
#De R$(1.621,01aR$) 2.902,84: 9%
#Acima de R$ 2.902,84: 14%

#VALE TRASPORTE
#Até R$ 1.621,00: 4%
#De R$(1.621,01aR$) 2.902,84: 5%
#Acima de R$ 2.902,84: 6%

#use (if / elif / else)
print("\n")
print("-- Verifique o salário líquido e os descontos --")
sal = float(input("Digite o seu salário: ").replace(",","."))

if sal >= 2902.84:
    print((f"\nINSS é R${sal * 0.14:.2f}").replace(".",","))
    print((f"Vale transporte é R${sal * 0.07:.2f}").replace(".",","))
    print((f"Salário líquido é R${sal - (sal * (0.14 + 0.07)):.2f}").replace(".",","))
elif sal >= 1621.01:
    print((f"INSS é R${sal * 0.09:.2f}").replace(".",","))
    print((f"Vale transporte é R${sal * 0.06:.2f}").replace(".",","))
    print((f"Salário líquido é R${sal - (sal * (0.09 + 0.06)):.2f}").replace(".",","))
else:
    print((f"INSS é R${sal * 0.075:.2f}").replace(".",","))
    print((f"Vale transporte é R${sal * 0.04:.2f}").replace(".",","))
    print((f"Salário líquido é R${sal - (sal * (0.075 + 0.04)):.2f}").replace(".",","))
print("\n")
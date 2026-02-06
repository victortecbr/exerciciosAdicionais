#Peça o nome de um mês e informe a estação do ano
mes = input("Insira um mês do ano: ").lower()
if mes in ["dezembro", "janeiro", "fevereiro"]:
    print("Verão.")
elif mes in ["março", "abril", "maio"]:
    print("Outono.")
elif mes in ["junho", "julho", "agosto"]:
    print("Inverno.")
elif mes in ["setembro", "outubro", "novembro"]:
    print("Primavera.")
else:
    print("Digitação invalida")
#Peça a temperatura em °C e diga se está frio (<18), 
# agradável (18/30) ou quente (>30).
temp = float(input("Digite a temperatura em °C: "))
if temp > 30 :
    print("Quente.")
elif temp >= 18:
    print("Agradável.")
else:
    print("Frio.")

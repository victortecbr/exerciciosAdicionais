# 2.Leia um valor em reais e mostre o valor convertido para dólar (cotação fixa definida no código).

print("-- Converta Real em Dolar --")
real = float(input("Digite o valor em Real R$:").replace(",","."))
conversao = 0.1901140684410646 #No dia 02/02/2026

print(f"A taxa de conversão atual é de {conversao:.2f}")
print(f"Assim você tem ${real * conversao:.2f} Dolares".replace(".",","))
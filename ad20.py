#Criar um programa que ajude um pescador a controlar sua produtividade.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de Santa Catarina (100 quilos), deve pagar
# uma multa de R$ 4,00 por quilo excedente. O pescador precisa que você faça
# um programa que leia o peso de peixes pescados no dia e verifique se há
# excesso. Se houver peso excedente, mostrar o valor que ele pagará de multa;
# caso contrário, mostrar uma mensagem dizendo que ele não deve pagar nada
# (resolver a questão utilizando uma função para calcular a multa caso seja
# necessário).

def calcular_multa(peso):
    limite = 100
    valor_multa = 4.00

    if peso > 100:
        excesso = peso - limite
        multa = excesso * valor_multa
        return excesso, multa
    
    else:
        return 0
    
peso = float(input("Digite o peso do pescado (Kg): "))
excesso, multa = calcular_multa(peso)

if multa > 0:
    print(f"Excesso de pescado: {excesso:.2f}")
    print(f"Multa a pagar: R${multa:.2f}")
else:
    print("Sem multa")





    
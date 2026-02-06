#Crie um sistema de login, onde:
#o usuário tem 3 tentativas
#login correto: admin
#senha correta: 1234

print("\n")
print("Digite seu usuário e senha")
usuario = input("Digite o seu usuario: ")
senha = input("Digite a sua senha: ")
i = 2

while i >= 1:
    if usuario == "admin" and senha == "1234":
        print("Acesso Liberado")
        break
    else:
        print(f"\nusuario ou senha inválidos você tem mais {i} tentativas")
        i -= 1
        usuario = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")
    print("\nNúmero de tentativas excedidas, aguarde 20 minutos e tente novamente")
print("\n")
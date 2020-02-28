usu = int(input("Digite o código de usuário:"))

if usu == 1234:
    senha = int(input("Digite sua senha:"))

    if senha == 9999:
        print("Acesso permitido")
    else:
        print("Acesso negado, senha incorreta!")
else:
    print("Código de usuário incorreto!")

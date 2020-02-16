while True:

    #Entrada de dados
    x = int(input("Digite um numéro inteiro:"))

    #Calculo quadrado e cubo

    q = x**2
    c = x**3

    print("O numéro elevado ao quadrado: %d, numéro elevado ao cubo: %d." %(q, c))

    #Verificando
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break

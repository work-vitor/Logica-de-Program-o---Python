while True:

    #Entrada de dados
    n1 = float(input("Insira um numéro:"))
    n2 = float(input("Insira outro numéro:"))

    #caculo media
    total = (n1+n2)/2

    #Resultado
    print("Média dos valores inseridos: %2.2f." %total)

    #Verificando
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break

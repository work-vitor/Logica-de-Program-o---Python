while True:
    num1 = float(input("Insira um numéro:"))
    num2 = float(input("Insira outro numéro:"))

    #Calculo
    soma = num2 + num1
    total = soma/2

    #Resultado
    print("Valor da soma dos dois numéros: %2.2f" %soma)
    print("Metade do Valor da soma dos dois numéros: %2.2f" %total)

    #Verificando
    veri = str(input("Deseja utilizar o sistema de novo S/N:"))

    if(veri == "N"):
        break

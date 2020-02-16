while True:

    #Entradsba de Dados
    ht = int(input("Insira quantas hora você trabalhou no mês:"))
    vh = float(input("Insira o valor pago por horas trabalhadas:"))
    pd = float(input("Insira o porcentual de desconto:"))

    #Calculo dos Dados
    sb = ht*vh
    por = (sb*pd)/100
    sl = sb - por

    #Apresentando Valores
    print("Salário Bruto: R$%2.2f, valor de desconto: R$%2.2f, Salário liquido: R$%2.2f" %(sb, por, sl))

   
    #Verificando
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break

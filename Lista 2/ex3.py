while True:
    ma = float(input("Digite quantos kg de maça deseja adquirir:"))
    mo = float(input("Digite quantos kg de morando deseja adquirir:"))

    if(ma <= 5) and (mo <=5):
        kg_total = ma + mo
        valor = (ma*1.80) + (mo*2.50)

        if(kg_total > 8) or (valor > 25):
            desconto = (valor *10)/100
            des = valor - desconto
            print("Total a pagar: R$%2.2f" %des)

        else:
            print("Total a pagar: R$%2.2f" %valor)

    else:
        kg_total = ma + mo
        valor = (ma*1.50) + (mo*2.20)

        if(kg_total > 8) or (valor > 25):
            desconto = (valor *10)/100
            des = valor - desconto
            print("Total a pagar: R$%2.2f" %des)

        else:
            print("Total a pagar: R$%2.2f" %valor)


    #Verificando while
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break
    
    

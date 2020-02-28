while True:

    #Entrada de dados
    com = str(input("Deseja colocar Álcool/Gasolina?"))
    quan = int(input("Informe quantos litros deseja:"))

    #Verificação
    if(com == "Álcool"):
        if(quan <= 20):
            val_al1 = quan * 2.90
            por = (val_al1*3)/100
            to1 = val_al1 - por

            #Resultado
            print("Total a ser pago: R$%2.2f." %to1)

        else:
            val_al2 = quan * 2.90
            por2 = (val_al2*5)/100
            to2 = val_al2 - por2

            #Resultado
            print("Total a ser pago: R$%2.2f." %to2)

    else:
         if(quan <= 20):
            val_gas = quan * 3.30
            por3 = (val_gas*4)/100
            to3 = val_gas - por3

            #Resultado
            print("Total a ser pago: R$%2.2f." %to3)

         else:
             val_gas1 = quan * 3.30
             por4 = (val_gas1*6)/100
             to4 = val_gas1 - por4

             #Resultado
             print("Total a ser pago: R$%2.2f." %to4)

    #Verificando while
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break

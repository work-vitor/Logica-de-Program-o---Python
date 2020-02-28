while True:
    nome = str(input("Digite o nome do produto:"))
    quant = int(input("Digite a quantidade adquirida:"))
    valorU = float(input("Digite o valor unitário:"))

    if(quant <=5):
        pre = quant *valorU
        des = (pre*2)/100
        to = pre - des

        print("Valor total a pagar sem desconto: R$%2.2f, com desconto de 2 porcento: R$%2.2f" %(pre, to))

    elif(quant > 5 ) and (quant <= 10):
        pre = quant *valorU
        des = (pre*3)/100
        to = pre - des

        print("Valor total a pagar sem desconto: R$%2.2f, com desconto de 3 porcento: R$%2.2f" %(pre, to))

    else:
        pre = quant *valorU
        des = (pre*5)/100
        to = pre - des

        print("Valor total a pagar sem desconto: R$%2.2f, com desconto de 5 porcento: R$%2.2f" %(pre, to))

    #Verificando while
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break


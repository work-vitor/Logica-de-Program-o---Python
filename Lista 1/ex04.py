#Entrada de Dados
fabri = float(input("Digite o valor de frabrica:"))

while True:
    #Calculo do distribuidor e impostos

    reaju = (fabri * 28) /100 + (fabri*45) /100
    total = fabri + reaju

    #Valor total do carro
    print("Valor total do carro: R$%2.2f" %total)

    quest = str(input("Deseja Calcular um novo valor S/N?"))

    if(quest == "S"):
        fabri = float(input("Digite o valor de frabrica:"))
    else:
        print("Sistena encerrado")
        break
    

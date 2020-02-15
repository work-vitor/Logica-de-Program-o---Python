while True:
    #Entrada de dados
    base = float(input("Insira o valor da base:"))
    altura = float(input("Insira a altura:"))

    #Calculo da área
    area = (base*altura)/2

    print("Área é igual: %2.2f" %area)

    #condição
    condi = str(input("Deseja fazer uma nova consulta S/N?"))
    
    if(condi == "N"):
        print("Sistena encerrado.")
        break

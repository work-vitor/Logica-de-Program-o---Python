while True:
    print("A média necessária para passar é igual a 25.")
    #Entrada de dados
    nota1 = float(input("Insira a primeira nota:"))
    nota2 = float(input("Insiara a segunda nota:"))
    nota3 = float(input("Insira a terceira nota:"))

    #Calculo da média
    media = (nota1 * 2) + (nota2 * 3) + (nota3 * 5) /100
    print("A média do aluno: %2.2f" %media)

    #Verificando se passou ou não
    if (media >= 25):
        print("Aluno Aprovado! :)")
    else:
        print("ALuno reprovado! :(")

    #Continua ou nao

    veri = str(input("Deseja ver mais umaa nota S/N?"))

    if(veri == "N"):
        break
    

while True:
    h1 = int(input("Digite a idade do primeiro homem:"))
    h2 = int(input("Digite a idade do segundo homem:"))
    m1 = int(input("Digite a idade da primeira mulher:"))
    m2 = int(input("Digite a idade da segunda mulher:"))

    if(h1 == h2) or (m1 == m2):
        print("Informe idades diferentes!!")
        break

    else:
        if(h1 > h2) and (m1 > m2):
            so1 = h1 + m2
            so2 = h2 + m1
            print("Valor da soma entra o homem mais velho e a mulher mais nova: %d" %so1)
            print("Valor da soma entre o homem mais nova e a mulher maus velha: %d" %so2)

        elif(h2> h1) and (m2 > m1):
            so1 = h2 + m1
            so2 = h1 + m2
            print("Valor da soma entra o homem mais velho e a mulher mais nova: %d" %so1)
            print("Valor da soma entre o homem mais nova e a mulher maus velha: %d" %so2)

        elif(h1> h2) and (m2 > m1):
            so1 = h2 + m1
            so2 = h1 + m2
            print("Valor da soma entra o homem mais velho e a mulher mais nova: %d" %so1)
            print("Valor da soma entre o homem mais nova e a mulher maus velha: %d" %so2)

    #Verificando while
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break
            

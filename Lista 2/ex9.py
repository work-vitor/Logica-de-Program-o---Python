while True:

    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    n3 = float(input("Digite a terceira nota:"))
    ex = float(input("Digite a média dos exercícios:"))

    #calculo

    mp = (n1+n2*2+n3*3+ex)/7

    #verificação
    if(mp >= 9):
        print("Seu conceito de aproveitamento foi: A")

    elif(mp >=7.5) and (mp <9):
        print("Seu conceito de aproveitamento foi: B")

    elif(mp >= 6) and (mp <7.5):
        print("Seu conceito de aproveitamento foi: C")

    else:
        print("Seu conceito de aproveitamento foi: D")

    #Verificando while
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break
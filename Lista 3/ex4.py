while True:

    codigo = int(input("Digite o código do aluno:"))

    #Verficando a pausa no while 
    if(codigo == 999):
        break

    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    n3 = float(input("Diigte a terceira nota:"))

    if(n1 > n2) and (n1 > n3):
        media = ((n1*4) + (n2*3) + (n3*3))/10

        if(media>=5):
            print("Aluno %d, teve a média: %.2f e está aprovado!" %(codigo, media))

        else:
            print("Aluno %d, teve a média: %.2f e está reprovado!" %(codigo, media))

    elif(n2 > n1) and (n2 > n3):
        media = ((n2*4) + (n1*3) + (n3*3))/10

        if(media>=5):
            print("Aluno %d, teve a média: %.2f e está aprovado!" %(codigo, media))

        else:
            print("Aluno %d, teve a média: %.2f e está reprovado!" %(codigo, media))

    elif(n3 > n1) and (n3 > n2):
        media = ((n1*3) + (n2*3) + (n3*4))/10

        if(media>=5):
            print("Aluno %d, teve a média: %.2f e está aprovado!" %(codigo, media))

        else:
            print("Aluno %d, teve a média: %.2f e está reprovado!" %(codigo, media))

    else:
        media = ((n1*3) + (n2*3) + (n3*3))/9

        if(media>=5):
            print("Aluno %d, teve a média: %.2f e está aprovado!" %(codigo, media))

        else:
            print("Aluno %d, teve a média: %.2f e está reprovado!" %(codigo, media))

    
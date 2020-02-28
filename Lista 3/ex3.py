c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
branco = 0
while True:
    voto = int(input("Digite seu voto:"))

    if (voto == 1):
        c1 = c1+1

    elif(voto == 2):
        c2 = c2 +1

    elif(voto == 3):
        c3 = c3+1
    
    elif(voto == 4):
        c4 = c4+1

    elif(voto == 5):
        nulo = nulo+1
    
    elif(voto == 6):
        branco = branco + 1

    elif(voto == 0):
        print("Total de votos!")
        print("Candidato 1: %d" %c1)
        print("Candidato 2: %d" %c2)
        print("Candidato 3: %d" %c3)
        print("Candidato 4: %d" %c4)
        print("Votos nulos: %d" %nulo)
        print("Votos em Branco: %d" %branco)
        break
    
    else:
        print("Digite um número válido, esse candidato não existe!")
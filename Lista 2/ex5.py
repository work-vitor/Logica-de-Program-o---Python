n1 = str(input("Digite o nome do time 1:"))
n2 = str(input("Digite o nome do time 2:"))

g1 = int(input("Digite o total de gols do time 1:"))
g2 = int(input("Digite o total de gols do time 2:"))

if(g1>g2):
    print("O time %s ganhou a partida." %n1)

elif(g1 == g2):
    print("Houve um empate!")
    
else:
    print("O time %s ganhou a partida." %n2)


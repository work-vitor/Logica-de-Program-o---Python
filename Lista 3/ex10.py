con = 0
maior = 0
menor = 99999999
md = 0
while con < 3:
    con = con+1
    num = int(input("Digite um numéro positivo:"))

    if(num < 0):
        print("Digite um numéro valido!")
        break
     
    md = md + num
    media = md/con

    if(num > maior):
        maior = num

    if(num < menor):
        menor = num

    if(con == 3):
        print("Maior numéro digitado: %d" %maior)
        print("Menor numéro digitado: %d" %menor)
        print("Média dos numéros digitados: %.2f" %media)

    
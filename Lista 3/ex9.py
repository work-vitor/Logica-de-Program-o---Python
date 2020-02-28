con = 0
ne = 0
while con < 5:
    con = con+1
    num = int(input("Digite um numéro:"))

    if(num < 0):
        ne = ne+1

print("Total de numéros negativos digitado: %d" %ne)
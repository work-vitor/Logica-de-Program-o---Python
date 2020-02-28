con = 0
p = 0
i = 0
while con < 5:
    con = con+1
    num = int(input("Digite um numéro inteiro:"))

    cal = num%2

    if(cal == 0):
        p = p+1
    
    if(cal == 1):
        i = i+1

print("Total de numéros pares digitados: %d" %p)
print("Total de numéros impares digitados: %d" %i)
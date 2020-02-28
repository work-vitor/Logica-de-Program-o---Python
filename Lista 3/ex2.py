x = 0
c = 0
n = int(input("Digite numéros inteiros e positivos:"))
while True:
    x = x+n
    c= (c+1)
    n = int(input("Digite numéros inteiros e positivos:"))
    
    

    if (n <= 0):
        m= x/c
        print("Média dos numéros digitados: %.2f" %m)
        break

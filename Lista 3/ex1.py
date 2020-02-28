ze = 1.10
chi = 1.50
x = 0
while (ze < chi):
    ze = ze + 0.3
    chi = chi + 0.2
    x = x+1
    print("Altura do Zé: %.2f, Altura do Chico: %.2f" %(ze, chi))
    print("Total de anos até Zé alcançar Chico: %d" %x)

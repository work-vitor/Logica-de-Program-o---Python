con = 0
maior = 0
menor = 99999999999999
while con <20:
    con = con + 1
    num = int(input("Digite um número inteiro:"))

    if num > maior:
        maior = num

    if num < menor:
        menor = num

print("Maior numéro digitado: %d" %maior)
print("Menor numéro digitado: %d" %menor)

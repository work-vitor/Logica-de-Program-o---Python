valor = 0
con = 0
print("Lojas Tabajara")
while True:

    pro = float(input("Digite o valor do produto:"))
    con = con + 1
    valor = valor+pro

    print("Produto %d: R$ %.2f" %(con, valor))

    if(pro == 0):
        print("Total: R$ %.2f" %valor)
        di = float(input("Informe o valor dado pelo cliente:"))

        troco = di - valor

        print("Troco: R$ %.2f" %troco)
        break
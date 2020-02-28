con = 0
pre = float(input("Informe o valor unitario do pão:"))

while con < 50:
    print("Preço do pão: R$%.2f" %pre)
    print("Panificadora Pão de Ontem - Tabela de preços")

    con = con + 1
    pao = pre * con

    print("%d - R$ %.2f" %(con, pao))
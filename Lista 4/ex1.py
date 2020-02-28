while True:
    num = int(input("Insira um numéro entre 0 e 10:"))

    if(num < 0) or (num > 10):
        print("Numéro inválido!")
        break
#Ponto inicial
deci = str(input("O reajuste é Negativo ou Positivo:"))

if(deci == "Negativo"):

    salario = float(input("Insira o valor do seu salário:"))
    valor_re = float(input("Insira o valor do reajuste:"))

    #Operação
    real = (salario*valor_re)/100
    novo_sal = salario-real

    print("Novo sálario: R$%2.2f, valor do reajuste: R%2.2f " %(novo_sal, real))

elif(deci == "Positivo"):
    salario = float(input("Insira o valor do seu salário:"))
    valor_re = float(input("Insira o valor do reajuste:"))

    # Operação
    real = (salario * valor_re) / 100
    novo_sal = salario + real

    print("Novo sálario: R$%2.2f, valor do reajuste: R%2.2f " %(novo_sal, real))

else:
    print("Por favor insira a informação correta!")

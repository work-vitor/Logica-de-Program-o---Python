while True:

    nome = str(input("Informe seu nome:"))

    n1 = len(nome)

    if(n1 > 3):
        idade = int(input("Informe sua idade:"))

        if(idade >= 0) and (idade <= 150):
            sal = float(input("Informe seu salário:"))
            
            if(sal > 0):
                sexo = str(input("Informe seu sexo F/M:"))
                sexo1 = sexo.upper()
                
                if(sexo1 == "F") or (sexo1 == "M"):
                    estadoC = str(input("Informe seu estado civil S, C, V ou D:"))
                    es = estadoC.upper()

                    if(es == "S") or (es == "C") or (es == "V") or (es == "D"):
                        print("Todas as informações estão corretas!")
                        break
                    else:
                        print("Informação inválida!")
                else:
                    print("Informação inválida!")  
            else:
                print("Informação inválida!") 
        else:
            print("Informação inválida!")
            
    else:
        print("Informação inválida!")
while True:

    co = int(input("Digite seu código de funcionário:"))
    na = int(input("Digite seu ano de nascimento:"))
    em = int(input("Digite seu ano de ingresso na empresa:"))
    ano = int(input("Digite o ano atual:"))

    #Calculo
    idade = ano - na
    empre = ano - em

    if( idade >= 60) and (empre >= 25):
        print("Voce tem %d anos e %d anos trabalhado na empresa." %(idade, empre))
        print("Requerer Aposentadoria.")

    else:
        print("Não requerer!")


     #Verificando while
    veri1 = str(input("Deseja utilizar o sistema de novo S/N:"))

    veri = veri1.upper()

    if(veri == "N"):
        print("Sistema encerrado.")
        break



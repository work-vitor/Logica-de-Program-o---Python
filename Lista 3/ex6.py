seco_bixo = 0
idade = 1
maior = 0

while idade>0:
    idade = int(input("Digite sua idade:"))
    if idade>0:
        sexo = str(input("Informe seu sexo:"))
        sexo1 = sexo.upper()
        
        olho = str(input("Informe cor dos olhos A-azuis, V-verdes ou C-castanhos:"))
        olho1 = olho.upper()

        cabelo = str(input("Informe a cor do cabelo L-louros, C-castanhos ou P-pretos:"))
        cabelo1 = cabelo.upper()

        if(idade>maior):
            maior = idade

        if(sexo1 == "FEMININO") and (idade >=18) and (idade <=35) and (olho1 == "V") and (cabelo1 == "L"):
            seco_bixo = seco_bixo+1

print("Maior idade: %d anos" %maior)
print("quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros: %d pessoas." %seco_bixo)

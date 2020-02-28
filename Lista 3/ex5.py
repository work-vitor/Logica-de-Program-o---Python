ce = 0
muie = 0
ca = 0
idade = 1
maior = 0
menor = 999
while idade>0:
    idade = int(input("Digite sua idade:"))
    if(idade > 0):
        sexo = str(input("Digite seu sexo:"))
        sal = float(input("Digite seu salário:"))
        
        ca = ca+sal
        ce = ce+1

        media = ca/ce


        sexo1 = sexo.upper()

        if( sexo1 == "FEMININO") and (sal <= 100):
            muie = muie+1

        if idade>maior:
            maior = idade

        if idade<menor:
            menor = idade

print("Média de salário: %.2f" %media)
print("Quantidade de mulheres que ganham até R$100: %d" %muie)   
print("Maior idade do grupo: %d anos" %maior)
print("Menor idade do grupo: %d anos" %menor)

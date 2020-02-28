ci = 0
aci = 0
rs = 0
maior = 0
menor = 99999
cidade = 0
while cidade < 5:
    cidade = cidade+1

    codigo = int(input("Digite o código da cidade:"))
    estado = str(input("Informe o estado, RS, SC PR, SP e RJ:"))

    estado1 = estado.upper()

    nv = int(input("Numéro de veículos de passeio:"))
    ind = int(input("Número de acidentes de trânsito com vítimas:"))

    ci = ci+nv
    media = ci/cidade

    if (ind >maior):
        maior = ind

    if(ind < menor):
        menor = ind

    if(estado1 == "RS"):
        aci = aci+1
        rs = rs + ind
        md = rs/aci


print("Menor índice de acidentes: %.2f e Maior índice de acidentes: %.2f" %(menor, maior))
print("Média de veículos nas cidades brasileiras: %.2f" %media)
print("Média de acidentes com vítimas entre as cidades do Rio Grande do Sul: %.2f" %md)
        

    

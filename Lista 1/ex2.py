#Entrada de dados
ano = int(input("Insira quantos anos você tem:"))
mes = int(input("Insira os meses:"))
dia = int(input("Insira os dias:"))

#Operações para o calculo

R = (ano*365) + (mes*30) + dia

print("Sua idade total expressa em dias: %d" %R)


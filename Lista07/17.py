#17.Um armazém trabalha com 100 mercadorias diferentes identificadas pelos números inteiros de 1 a 100.
#O dono do armazém anota a quantidade de cada mercadoria vendida durante o mês.
#Ele tem uma tabela que indica, para cada mercadoria, o preço de venda. 
#Escreva um algoritmo para calcular o faturamento mensal do armazém. 
#A tabela de preços é fornecida seguida pelos números das mercadorias e as quantidades vendidas.
#Quando uma mercadoria não tiver nenhuma venda, é informado o valor zero no lugar da quantidade.


NUM = []
QTD = []
VALOR = []

for i in range(100):
    NUM.append(int(input("Informe o numero da mercadoria: ")))
    while True:
        cont = 0
        for k in range(len(NUM)):
            if NUM[i] == NUM[k]:
                cont += 1
        if cont > 1:
            NUM[i] = int(input("Mercadoria ja cadastrada, Informe o numero da nova mercadoria: "))
        else:
            break
    QTD.append(int(input("Informe a quantidade vendida: ")))
    VALOR.append(int(input("O Valor unitario da mercadoria: ")))


for i in range(len(NUM)):
    print("Mercadoria:",NUM[i])
    print("Quatidade Vendida:", QTD[i])
    print("Valor Total:", VALOR[i]*QTD[i])
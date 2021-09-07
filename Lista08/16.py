#16. Crie um algoritmo que carregue uma matriz 12 x 4 com os valores das vendas
#de uma loja, em que cada linha represente um mês do ano, e cada coluna, uma
#semana do mês. Para fins de simplificação considere que cada mês possui somente
#4 semanas. Calcule e escreva:
#● Total vendido em cada mês do ano;
#● Total vendido em cada semana durante todo o ano;
#● Total vendido no ano.

matriz = [[0 for j in range(4)] for i in range(12)]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor o mes {i} da semana {j}: "))

Tano = 0
for i in range(len(matriz)):
    Total = 0
    for j in range(len(matriz[i])):
        Total += matriz[i][j]
        print(f"Foram feitas {matriz[i][j]} vendas na semana {j} do mes {i} ")
    print(f"Foram feitas {Total} vendas no mes {i}")
    Tano += Total
print(f"Foram feitas {Tano} vendas no ano")
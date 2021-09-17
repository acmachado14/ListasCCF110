#14. Crie um algoritmo que leia uma matriz A[NxN] (N ≤ 10) e verifique (informe) se
#tal matriz é ou não simétrica (At = A).

N = int(input("Escreva o numero de linhas/colunas de sua matriz NxN: "))

matriz = [[0 for j in range(N)] for i in range(N)]
matrizT = [[0 for j in range(N)] for i in range(N)]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
        matrizT[j][i] = matriz[i][j]

for i in range(len(matrizT)):
    for j in range(len(matrizT[i])):
        if(j == len(matrizT[i]) -1):
            print("%d" %matrizT[i][j])
        else:
            print("%d" %matrizT[i][j], end = " ")


cont = 0
for i in range(len(matrizT)):
    for j in range(len(matrizT[i])):
        if matrizT[i][j] != matriz[i][j]:
            cont +=1

if cont == 0:
    print("Sao simetricas!!!  XD")
else:
    print("Nao sao simetricas... ;-;")
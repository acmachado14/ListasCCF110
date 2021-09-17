#16. Crie um algoritmo que leia uma matriz A[2x2] e calcule a respectiva inversa A-1.

matriz = [[0 for j in range(2)] for i in range(2)]
matrizIn = [[0 for j in range(2)] for i in range(2)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))

matrizIn[0][0] = matriz[1][1]
matrizIn[1][1] = matriz[0][0]

for i in range(len(matrizIn)):
    for j in range(len(matrizIn[i])):
        if i + j == len(matrizIn)-1:
            matrizIn[i][j] = -1 * matriz[i][j] 

for i in range(len(matrizIn)):
    for j in range(len(matrizIn[i])):
        if(j == len(matrizIn[i]) -1):
            print("%d" %matrizIn[i][j])
        else:
            print("%d" %matrizIn[i][j], end = " ")
print()


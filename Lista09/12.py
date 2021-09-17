#12. Crie um algoritmo que leia valores para uma matriz M[2x2]. Calcule e escreva o
#determinante. Para cálculo do determinante de uma matriz de ordem 2, é
#simplesmente computar a diferença entre os produtos das diagonais principal e
#secundária, respectivamente.


matriz = [[0 for j in range(2)] for i in range(2)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))

prod2 = 1
prod1 = 1
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            prod1 = matriz[i][j] * prod1
        elif i + j == len(matriz)-1:
            prod2 = matriz[i][j] * prod2

print (f"A diferença é de {prod1-prod2}")
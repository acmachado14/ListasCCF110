#1. Crie um algoritmo que leia uma matriz 5x5 e escreva na tela o item na última
#posição de cada linha dessa matriz.

M = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        M[i][j] = int(input("Numero"))
        if j == 4:
            print(M[i][j])
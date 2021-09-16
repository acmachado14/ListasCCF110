#Crie um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
#somente os elementos abaixo da diagonal principal.

matriz = [[0 for j in range(10)] for i in range(10)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i+1},{j+1}): "))

#A cima da diagonal principal é quando os i for uma unidade maior que os j, exemplo: 1,0 2,1 3,2 ....
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if (i - j) == 1:
            print(matriz[i][j])

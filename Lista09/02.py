#Crie um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
#somente os elementos abaixo da diagonal principal.

matriz = [[0 for j in range(10)] for i in range(10)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i+1},{j+1}): "))

#Diagonal principal é quando os i for igual a j, exemplo: 1,1 2,2 3,3 .....
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i < j:
            print(matriz[i][j])


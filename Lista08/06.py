#6. Crie um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
#a soma dos elementos que estão acima da diagonal principal.

matriz = [[0 for j in range(10)] for i in range(10)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i+1},{j+1}): "))

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i < j:
            soma += matriz[i][j]

print(f"A soma dos valores é: {soma}")
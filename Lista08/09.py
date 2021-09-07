#9. Entre com valores para uma matriz A[3x4]. Gere e escreva uma matriz B que é o
# triplo da matriz A.

matriz = [[0 for j in range(4)] for i in range(3)]
B = [[0 for j in range(4)] for i in range(3)]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i+1},{j+1}): "))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        B[i][j] =  matriz[i][j] * 3

print()

for i in range(len(B)):
        for j in range(len(B[i])):
            if(j == len(B[i]) -1):
                print("%d" %B[i][j])
            else:
                print("%d" %B[i][j], end = " ")
print()

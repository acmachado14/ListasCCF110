# 11. Entre com valores para duas matrizes inteiras de ordem cinco. Gere e escreva a
# matriz diferença.

A = [[0 for j in range(4)] for i in range(4)]
B = [[0 for j in range(4)] for i in range(4)]
C = [[0 for j in range(4)] for i in range(4)]

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = int(input(f"Digite o valor para A[{i+1}][{j+1}]: "))

for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j] = int(input(f"Digite o valor para B[{i+1}][{j+1}]: "))

for i in range(len(C)):
    for j in range(len(C[i])):
        C[i][j] = A[i][j] - B[i][j]

print()

for i in range(len(B)):
        for j in range(len(B[i])):
            if(j == len(B[i]) -1):
                print("%d" %B[i][j])
            else:
                print("%d" %B[i][j], end = " ")
print()

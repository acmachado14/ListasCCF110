#10. Entre com valores inteiros para uma matriz A[4x4] e para uma matriz B[4x4].
# Gere e escreva a SOMA (A + B).

A = [[0 for j in range(4)] for i in range(4)]
B = [[0 for j in range(4)] for i in range(4)]
soma = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = int(input(f"Digite o valor para A[{i+1}][{j+1}]: "))
        soma += A[i][j]

for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j] = int(input(f"Digite o valor para B[{i+1}][{j+1}]: "))
        soma += B[i][j]

print(soma)
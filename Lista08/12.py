#12. Leia uma matriz 4x5 de inteiros, calcule e escreva a soma de todos os seus
#elementos.

A = [[0 for j in range(5)] for i in range(4)]
soma = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = int(input(f"Digite o valor para A[{i+1}][{j+1}]: "))
        soma += A[i][j]

print(soma)
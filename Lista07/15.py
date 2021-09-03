#15. Fazer algoritmo que:
#a) Leia o valor inteiro de n (n ≤ 1000) e os n valores de vetor de valores numéricos;
#b) Ordenar o vetor e escrevê-lo ordenado.
#c) Determine e escreva, para cada número que se repete no conjunto, a quantidade de vezes em que ele aparece repetido;

A = []
n = int(input())

while n > 1000:
    n = int(input())

for i in range(n):
    A.append(int(input()))

for i in range(n):
    aux = 0
    for j in range(n-1):
        if A[j] > A[j+1]:
            aux = A[j]
            A[j] = A[j+1]
            A[j+1] = aux

for i in range(n):
    print(A[i])

for i in range(n):
    repete = 0
    for j in range(n):
        if A[i] == A[j]:
            repete += 1
    print("O Numero", A[i] , "Se aparece", repete, " vezes")
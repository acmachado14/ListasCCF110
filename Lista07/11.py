#11. Fazer um algoritmo que:
#a)Leia o valor inteiro de n (n ≤ 1000) e os n valores de um vetor A de valores numéricos, ordenados de forma crescente;
#b)Determine e escreva, para cada número que se repete no conjunto, a quantidade de vezes em que ele aparece repetido;
#c)Elimine os elementos repetidos, formando um novo conjunto;
#d)Escreva o conjunto obtido.

#a)
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
#b)

for i in range(n):
    repete = 0
    for j in range(n):
        if A[i] == A[j]:
            repete += 1
    print("O Numero", A[i] , "Se aparece", repete, " vezes")


#c)

for i in range(n):
    for j in range(i+1, n):
        if A[j] == A[i]:
            for k in range(j, n-1):
                A[k] = A[k + 1]
            n -= 1
        else:
            j += 1

    
#d)

for i in range(n):
    print(A[i])
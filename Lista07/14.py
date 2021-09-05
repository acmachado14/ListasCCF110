#14. Faça um algoritmo que leia um valor N (N ≤ 20) e os N valores de um vetor. 
#Ordene os valores recebidos em forma crescente e decrescente e escreva os vetores ordenados.

n = int(input("Digite o numero de elementos que deseja armazenar: "))
while n > 20:
    n = int(input("Numero inválido!! Digite novamente: "))
    
A = []
for i in range(n):
    A.append(int(input(f"Informe o numero da posição A[{i+1}]: ")))
#----------------------------Crescente------------------------------


for i in range(n):
    aux = 0
    for j in range(n-1):
        if A[j] > A[j+1]:
            aux = A[j]
            A[j] = A[j+1]
            A[j+1] = aux

for i in range(n):
    print(f"A[{i+1}]: {A[i]}")

#----------------------------Decrescente------------------------------

print("Decrescente:")
for i in range(n):
    aux = 0
    for j in range(n-1):
        if A[j] < A[j+1]:
            aux = A[j]
            A[j] = A[j+1]
            A[j+1] = aux

for i in range(n):
    print(f"A[{i+1}]: {A[i]}")
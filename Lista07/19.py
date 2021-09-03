#Faça um algoritmo que leia um vetor (variável composta) de N valores numéricos (N ≤ 20) 
#ordene essa variável em ordem crescente.
#O programa também deve ler um número k, e escrever, antes e depois da ordenação, o k-ésimo termo da variável composta.


V = []
n = int(input("Digite o tamanho do vetor: "))
while n >= 20:
    n = int(input())
k = int(input("Digite o k-ésimo termo que quer encontrar: "))

for i in range(n):
    V.append(int(input(f"Digite o {i+1} valor: " )))

print("Antes da ordenação o k-ésimo era este:", V[k-1])

for i in range(n):
    aux = 0
    for j in range(n-1):
        if V[j] > V[j+1]:
            aux = V[j]
            V[j] = V[j+1]
            V[j+1] = aux

print("Depois da ordenação o k-ésimo é este:", V[k-1])
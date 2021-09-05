#16. Dado um conjunto de 100 valores numéricos disponíveis num meio de entrada qualquer,
#fazer um algoritmo para armazená-los em um vetor B, e calcular e escrever o valor do somatório dado a seguir:
# S = (b1 - b100)³ + (b2 - b99)³ + ... + (b50 - b51)³

A = []
for i in range(6):
    A.append(int(input(f"Informe o numero da posição A[{i}]: ")))

S = 0
for i in range(6):
    S += ((A[i] - A[5-i])**3)

print(S)
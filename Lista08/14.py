#14. Crie um algoritmo que possa armazenar as alturas de dez atletas de cinco
#delegações que participarão dos jogos de verão. Armazene esses dados em uma
#matriz. Depois, escreva a maior altura de cada delegação.


#adotei como 10 atletas para cada delegação
A = [[0 for j in range(5)] for i in range(10)]
for j in range(len(A[0])):
    for i in range(len(A)):
        A[i][j] = int(input(f"Digite a altura do atleta {i+1} para A delegação {j+1}: "))

for j in range(len(A[0])):
    maior = 0
    for i in range(len(A)):
        if i == 0:
            maior = A[i][j]
        elif A[i][j] > maior:
            maior = A[i][j]
    print(f" O maior altura da delegação {j+1} é: {maior}")
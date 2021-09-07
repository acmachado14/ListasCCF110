#13. Leia valores inteiros para a matriz A[3x5]. Gere e escreva o vetor SL (soma das
#3 linhas), onde cada elemento é a soma dos elementos de uma linha da matriz A.
#Faça o trecho que gera a matriz SL separado (laços de repetição) da entrada e da
#saída de dados.

A = [[0 for i in range(5)] for j in range(3)]
vetorSL = [0 for i in range(3)]

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))

posicaoSl = 0
for i in range(len(A)):
    for j in range(len(A[0])):
        vetorSL[posicaoSl] += A[i][j]
    posicaoSl += 1

for i in range(len(vetorSL)):
    print(vetorSL[i])
#2. Crie um algoritmo que leia uma matriz 7x7 e um valor N e diga em qual posição
# da matriz, linha e coluna, esse valor N se encontra. Caso esse valor não esteja na
# matriz, imprima uma mensagem de erro.

matriz = [[0 for j in range(7)] for i in range(7)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i+1},{j+1}): "))

N = int(input("Digite o valor N a ser comparado"))

cont = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == N:
            print(f"O valor N encontra-se na posição:{i},{j}")
            cont += 1
if cont == 0:
    print("Nao existe!")
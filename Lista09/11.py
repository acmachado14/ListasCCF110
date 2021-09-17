#11. Crie um algoritmo que entre com valores inteiros para uma matriz M[3x3] e
#escreva a matriz final, conforme mostrado a seguir: 270°

matriz = [[0 for j in range(3)] for i in range(3)]
matriz90 = [[0 for j in range(3)] for i in range(3)]

coluna = -1
for i in range(len(matriz)):
    linha = (len(matriz)-1)
    coluna += 1
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
        matriz90[linha][coluna] = matriz[i][j]
        linha -= 1


for i in range(len(matriz90)):
    for j in range(len(matriz90[i])):
        if(j == len(matriz90[i]) -1):
            print("%d" %matriz90[i][j])
        else:
            print("%d" %matriz90[i][j], end = " ")
print()


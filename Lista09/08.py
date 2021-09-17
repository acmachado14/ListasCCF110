#8. Crie um algoritmo que leia e armazene os elementos de uma matriz inteira
#M[10x10] e escrevê-la. Troque, na ordem a seguir:
#   ● A segunda linha pela oitava linha;
#   ● A quarta coluna pela décima coluna;
#   ● A diagonal principal pela diagonal secundária

matriz = [[0 for j in range(10)] for i in range(10)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))

for j in range(len(matriz[0])):
    aux = matriz[1][j]
    matriz[1][j] = matriz[7][j]
    matriz[7][j] = aux

for i in range(len(matriz[0])):
    aux = matriz[i][3]
    matriz[i][3] = matriz[i][9]
    matriz[i][9] = aux

princ = []
second = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            princ.append(matriz[i][j])
        elif i + j == len(matriz)-1:
            second.append(matriz[i][j])


cont1 = 0
cont2 = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            matriz[i][j] = princ[cont1]
            cont1 += 1

        elif i + j == len(matriz)-1:
            matriz[i][j] = second[cont2]
            cont2 += 1


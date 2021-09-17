#17. Crie um algoritmo que receba duas matrizes A[CxD] e B[ExF] (C, D, E e F ≤ 6).
#Esse algoritmo deve verificar se o produto matricial de A por B é possível (D = E).
#Caso seja possível, calcular o tal produto, escrevendo a matriz G[CxF] resultado.

C = int(input("Digite o tamanho C da matriz CxD: "))
D = int(input("Digite o tamanho D da matriz CxD: "))

E = int(input("Digite o tamanho E da matriz ExF: "))
F = int(input("Digite o tamanho F da matriz ExF: "))

if (E == D):
    A = [[0 for j in range(D)] for i in range(C)]
    B = [[0 for j in range(F)] for i in range(E)]
    G = [[0 for j in range(F)] for i in range(C)]

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(input(f"Digite o valor para A[{i}][{j}]: "))

    print()

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = int(input(f"Digite o valor para B[{i}][{j}]: "))


    print()

    for i in range(len(G)):
        for j in range(len(G[i])):
            for k in range(D):
                G[i][j] += A[i][k] * B[k][j] 


    print()

    for i in range(len(G)):
        for j in range(len(G[i])):
            if(j == len(G[i]) -1):
                print("%d" %G[i][j])
            else:
                print("%d" %G[i][j], end = " ")
    
else:
    print("Nao é possivel realizar pois E != D")

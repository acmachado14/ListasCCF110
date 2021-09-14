#1. Primeiro criamos uma matriz com 3 colunas e 10 linhas. Depois lemos o
#nome, a idade e a altura das 10 pessoas. Em seguida buscamos em qual
#linha está a pessoa mais nova e a pessoa mais alta. Com isso podemos
#imprimir o nome dessas pessoas.

A = [[0 for j in range(3)] for i in range(2)]

for i in range(len(A)):
    A[i][0] = input("Digite o nome: " )
    A[i][1] = int(input("Digite a idade: " ))
    A[i][2] = int(input("Digite a altura: " ))


for i in range(len(A)):
    if i == 0:
        maisNova = i
        maisAlta = i
    elif A[i][1] > maisNova:
        maisNova = i
    elif A[i][2] > maisAlta:
        maisAlta = i

print(f"A pessoa mais nova esta na linha {maisNova}")
print(f"A pessoa mais alta esta na linha {maisAlta}")
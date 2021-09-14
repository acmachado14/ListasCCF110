#7. A matriz dados contém na 1ª coluna a matrícula do aluno no curso; na 2ª, o sexo
#(0 para feminino e 1 para masculino); na 3ª, o código do curso, e na 4ª, o CR
#(Coeficiente de Rendimento). Suponha 10 alunos e que o CR é um número inteiro.
#Um grupo empresarial resolveu premiar a aluna com CR mais alto de um curso cujo
#código deverá ser digitado. Faça um algoritmo que armazene esses dados
#sabendo-se que você deve:
#   ● Ler a matrícula. Ela é da seguinte forma: aascccnnn (aa ano, s semestre, ccc
#   código do curso e nnn matrícula no curso);
#   ● Ler o sexo (0 para feminino e 1 para masculino);
#   ● Ler o CR;
#   ● O código do curso é uma parte da matrícula, portanto não deve ser lido.
#   Retire essa informação da matrícula dada.
#   ● Leia o código do curso a ser premiado.
#   Mostre na tela a matrícula, o CR e o código da aluna premiada.

A = [[0 for j in range(4)] for i in range(2)]

for i in range(len(A)):
    A[i][0] = input("Digite a matricula do aluno: " )
    A[i][1] = int(input("Digite o sexo 0 - feminino 1 - masculino: " ))
    A[i][3] = int(input("Digite o coeficiente de rendimento: " ))
    matricula = A[i][0]
    A[i][2] = matricula[3] + matricula[4] + matricula[5]

aux = 0 
N = input("Digite o codigo do curso a ser avaliado: ")
for i in range(len(A)):
    if N in A[i][2] and A[i][1] == 0:
        if aux == 0:
            maior = A[i][3]
            mat = A[i][0]
            aux += 1
        elif A[i][3] > maior:
            maior = A[i][3]
            mat = A[i][0]

print(f"O maior CR: {maior} feminino foi da aluna {mat}")
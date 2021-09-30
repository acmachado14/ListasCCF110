#6. Faça um programa para alterar uma das notas de um aluno (usando os arquivos
#do exercício anterior). O programa deve receber o nome do aluno, a nota velha e a
#nova nota.


nomes = open("nomes", 'r')
notas = open("notas", '+r')
notas02 = open("notas_atualizadas", 'w')

n = input("Digite o nome do aluno: ") 
s = input("Digite as novas notas separadas por espaço: ")

posicao = 0
cont = 0
for nome in nomes:
    if n in nome:
        posicao = cont
    cont += 1

cont = 0

for nota in notas:
    if cont == posicao:
        notas02.write(s)
        notas02.write("\n")
    else:
        notas02.write(nota)
    cont +=1


nomes.close()
notas.close()
notas02.close()
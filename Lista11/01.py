#1. Faça um programa que escreve um arquivo com números em ordem decrescente
#de 200 a 50. Cada número deve estar em uma linha. Dê o nome que quiser para o
#arquivo.
nome = input()
arquivo = open(nome, 'w')
for i in range(200,50,-1):
    arquivo.write(str(i))
    arquivo.write("\n")
arquivo.close()
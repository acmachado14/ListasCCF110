#5. Faça um programa que recebe os nomes de dois arquivos. O primeiro arquivo
#contém nomes de alunos e o segundo arquivo contém as notas dos alunos. No
#primeiro arquivo, cada linha corresponde ao nome de um aluno e no segundo
#arquivo, cada linha corresponde às notas dos alunos (uma ou mais). Assuma que as
#notas foram armazenadas como strings, e estão separadas umas das outras por
#espaços em branco. Leia os dois arquivos e gere um terceiro arquivo que contém o
#nome do aluno seguido da média de suas notas.

nomes = open("nomes", 'r')
notas = open("notas", 'r')
arquivo = open("teste", 'w')

medias = []
for nota in notas:
    soma = 0
    cont = 0
    for x in nota.split():
        soma += int(x)
        cont += 1
    medias.append(soma/cont)

posicao = 0
for nome in nomes:
    s = nome + " Media: "
    arquivo.write(str(s))
    arquivo.write(str(medias[posicao]))
    arquivo.write("\n")
    posicao += 1

nomes.close()
notas.close()
arquivo.close()

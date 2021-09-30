#2. Faça um programa que leia um número N e gere um arquivo com N nomes e
#idades aleatórios:
#● Faça uso de duas listas criadas na mão: uma que contenha 20 nomes e outra
#que contenha 20 sobrenomes;
#● Cada linha do arquivo resultante deve conter um nome completo e a sua
#idade;
#● Todos os dados podem ser gerados no próprio código sem a necessidade de
#fazer a leitura por meio de um arquivo.
import random
N = int(input())
arquivo = open("teste", 'w')
nomes = ["Angelo","Alek", "Tayner", "Everson", "Julio", "Igor", "Gabriel", "Gabriela", "Fernanda" ,"Arthur", "Samuel", "Brenda", "Ingred", "Silvania", "Lorena", "Yasmim", "Cleber", "Erika", "Patricia", "Silvio"]
sobrenomes =["Cupertino", "Machado", "Silva", "Fernandes", "Bastos", "Werneck", "Pereira", "Ferreira", "Pires", "Reis", "Mafra","Barbosa", "Melo", "Viana", "Lima", "Pinto", "Marquezine", "Elias", "Grande", "Carvalho"]

for i in range(N):
    nome = nomes[random.randint(0, 19)] + " " + sobrenomes[random.randint(0, 19)]
    arquivo.write(nome)
    arquivo.write("\n")
    arquivo.write(str(random.randint(1, 35)))
    arquivo.write("\n")
arquivo.close()
    
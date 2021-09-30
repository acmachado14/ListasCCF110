#3. Estenda o exemplo do cadastro para considerar também a altura da pessoa
import random
N = int(input())
arquivo = open("teste", 'w')
nomes = ["Angelo","Alek", "Tayner", "Everson", "Julio", "Igor", "Gabriel", "Gabriela", "Fernanda" ,"Arthur", "Samuel", "Brenda", "Ingred", "Silvania", "Lorena", "Yasmim", "Cleber", "Erika", "Patricia", "Silvio"]
sobrenomes =["Cupertino", "Machado", "Silva", "Fernandes", "Bastos", "Werneck", "Pereira", "Ferreira", "Pires", "Reis", "Mafra","Barbosa", "Melo", "Viana", "Lima", "Pinto", "Marquezine", "Elias", "Grande", "Carvalho"]

for i in range(N):
    nome = nomes[random.randint(0, 19)] + " " + sobrenomes[random.randint(0, 19)]
    arquivo.write(nome)
    arquivo.write("\n")
    arquivo.write(str("Idade: "))
    arquivo.write(str(random.randint(1, 35)))
    arquivo.write("\n")
    arquivo.write(str("Altura: "))
    arquivo.write(str(random.randint(150, 200)))
    arquivo.write("\n")
arquivo.close()


    
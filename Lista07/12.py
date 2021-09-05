#12. Fazer um algoritmo que:
#Leia um conjunto de valores inteiros correspondentes a 80 notas dos alunos de uma turma, notas estas que variam de 0 a 10;
#Calcule a frequência absoluta e a frequência relativa de cada nota;
#Escreva uma tabela contendo os valores das notas (de 0 a 10) e suas respectivas frequências absoluta e relativa

vetor = []

for i in range(5):
    n = int(input(f"Digite a {i + 1}ª nota para o vetor:"))
    if 0 <= n <= 10:
        vetor.append(n)
    else:
        print("Nota inválida. Insira as notas novamente.")

for i in range(len(vetor)):
    repete = 0
    for j in range(len(vetor)):
        if vetor[i] == vetor[j]:
            repete += 1
    fr = repete / len(vetor)
    print(f"frequência absoluta de {vetor[i]} = {repete}")
    print(f"frequência relativa de {vetor[i]} = {fr}")
    print("-----------------------------------------")

#repare que as notas repitidas se repetem na saida dos dados. Nao acretido que isso seja tão significativo ent deixei assim mesmo
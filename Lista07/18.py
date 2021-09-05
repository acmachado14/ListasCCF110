#18. Numa corrida há 10 corredores, de número de inscrição de 1 a 10.
#Faça um algoritmo que leia os valores do tempo na corrida de cada corredor.
#O programa deve escrever a qualificação e o tempo de corrida, do primeiro ao décimo colocado,
#identificando o número de inscrição do corredor referente àquela colocação.
#Suponha que não há tempos iguais. (Dica: Utilize o índice do vetor para indicar o número de inscrição dele. 
#Note que se você ordenar o vetor original vai perder esse número.)


T = []
ID = []
for i in range(10):
    T.append(int(input(f"Informe o tempo de corrida do corredor {i}: ")))
    ID.append(i)

for i in range(len(T)):
    aux = 0
    auxId = 0
    for j in range(len(T)-1):
        if T[j] > T[j+1]:
            aux = T[j]
            T[j] = T[j+1]
            T[j+1] = aux

            auxId = ID[j]
            ID[j] = ID[j+1]
            ID[j+1] = auxId

for i in range(len(T)):
    print(f"{i+1} Lugar para o canditato {ID[i]}: {T[i]}")
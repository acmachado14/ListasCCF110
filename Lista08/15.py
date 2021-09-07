#15. A gerente do cabeleireiro Sempre Bela tem uma tabela em que registra os "pés",
#as “mãos” e “pés e mãos”. Sabendo-se que cada uma ganha 50% do que faturou ao
#mês, criar um algoritmo que possa calcular e escrever quanto cada um vai receber,
#uma vez que não têm carteiras assinadas; os valores, respectivamente, são R$
#10,00; R$ 15,00 e R$ 30,00.



N = int(input("Informe o numero de funcionarias: "))

T = [[0 for j in range(3)] for i in range(N)]

Nome = []
for i in range(N):
    Nome.append(input(f"Informe o nome da funcionária {i+1}: "))

    T[i][0] = int(input(f"Informe o numero de 'pés' feitos da Funcionaria {Nome[i]}: "))
    
    T[i][1] = int(input(f"Informe o numero de 'mão' feitos da Funcionaria {Nome[i]}: "))

    T[i][2] = int(input(f"Informe o numero de 'pés e mãos' feitos da Funcionaria {Nome[i]}: "))

    print (f"Funcionaria: {Nome[i]} Receberá de pés: {(T[i][0]*10)*0.5}, de mão: {(T[i][1]*15)*0.5}, de pés e mãos: {(T[i][2]*30)*0.5}")
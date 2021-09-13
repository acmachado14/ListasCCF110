#6. Uma floricultura conhecedora de sua clientela gostaria de fazer um algoritmo que
#pudesse controlar sempre um estoque mínimo de determinadas plantas, pois todo
#dia, pela manhã, o dono faz novas aquisições. Criar um algoritmo que deixe
#cadastrar 50 tipos de plantas e nunca deixar o estoque ficar abaixo do ideal. Para
#cada planta, o dono gostaria de cadastrar o nome, o estoque ideal e a quantidade
#em estoque. Dessa forma o algoritmo pode calcular a quantidade que o dono da loja
#precisa comprar no próximo dia. Essa quantidade a ser comprada deve ser escrita
#(quando maior que zero) como uma lista para o dono da floricultura.


F = [[0 for j in range(3)] for i in range(50)]

for i in range(len(F)):
        F[i][0] = input("Digite o nome da planta: " )
        F[i][1] = int(input("Digite a quantidade em estoque: " ))
        F[i][2] = int(input("Digite a quantidade ideal: " ))
        
print()

for i in range(len(F)):
    print(f"Para a planta: {F[i][0]} voce precisa comprar {F[i][2] - F[i][1]}")

print()

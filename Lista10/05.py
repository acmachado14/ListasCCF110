#5. Faça um programa que manipula uma lista que contém modelos de carro e seu
#consumo (km/l), da seguinte forma: [[‘Vectra’, 9], [‘Gol’, 10], [‘Corsa’, 11], [‘Fit’, 12.5]].
#Você deve ler as informações referentes aos veículos do teclado. Esses valores
#acima são apenas um exemplo para que você veja como devem estar organizadas
#as informações. O programa deve mostrar na tela o nome do modelo mais
#econômico. Além disso, deve mostrar na tela quanto cada um desses modelos
#gastaria para percorrer 1000 Km, assumindo que o valor do litro da gasolina é
#R$3,50.

carro = [[0 for i in range(2)] for j in range(3)]

for i in range(len(carro)):
    nome,L = input().split()
    carro[i][0] = nome
    carro[i][1] = int(L)

for i in range(len(carro)):
    if i == 0:
        maior = carro[i][1]
        Pmaior = i
    elif maior < carro[i][1]:
        maior = carro[i][1]
        Pmaior = i

for i in range(len(carro)):
    print(carro[i][0], end=" ")
    print(1000/(carro[i][1]) * 3.5)

print(f"O carro com o maior rendimento é o: {carro[Pmaior][0]}, com um consumo de {carro[Pmaior][1]}")
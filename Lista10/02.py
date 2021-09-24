#2. Faça um programa que percorre duas listas e intercala os elementos de ambas,
#formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da
#lista menor. Exemplo:
#lista1 = [1, 2, 3, 4]
#lista2 = [10, 20, 30, 40, 50, 60]
#lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]
import random

l1 = []
l2 = []
l3 = []

for i in range(random.randint(1, 6)):
    l1.append(random.randint(1, 6))

for i in range(random.randint(1, 6)):
    l2.append(random.randint(1, 6))

cont1 = 0
cont2 = 0
if len(l1) < len(l2):
    while True:
        if cont1 < len(l1):
            l3.append(l1[cont1])
        if cont2 < len(l2):
            l3.append(l2[cont2])
        else:
            break
        cont1 += 1
        cont2 += 1
else:
    while True:
        if cont1 < len(l1):
            l3.append(l1[cont1])
        else:
            break
        if cont2 < len(l2):
            l3.append(l2[cont2])  
        cont1 += 1
        cont2 += 1

for i in range(len(l3)):
    print(l3[i])


#1. Faça um programa que simule um lançamento de dados. Lance o dado 10 vezes
#e armazene os resultados em um vetor. Depois, monte um outro vetor contendo
#quantas vezes cada valor foi obtido. Imprima os dois vetores. Use uma função para
#gerar números aleatórios, simulando os lançamentos dos dados. Exemplo de uma
#possível saída:
#[3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
#[1, 0, 3, 1, 4, 1]

import random
v = []

for i in range(10):
    v.append(random.randint(1, 6))

x = []
for i in range(10):
    x.append(v.count(v[i]))

for i in range(10):
    print(v[i], end="")

print()

z = []

for i in x:
  if i not in z:
    z.append(i)

for i in range(len(z)):
    print(z[i], end="")

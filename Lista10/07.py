#7. Em uma universidade são distribuídas 300 senhas para a fila do bandejão, que
#funciona da seguinte forma: As filas começam a se formar pela manhã. Até às 11h,
#horário de abertura do restaurante, os alunos podem guardar lugar para no máximo
#3 outros colegas, depois disso a fila é congelada. Se a quantidade de pessoas na
#fila + lugares guardados ultrapassar 300, os extras ficarão sem senha.

#Escreva um programa que percorre uma lista com as matrículas dos alunos que
#estão aguardando na fila. Para cada aluno, começando do último, descubra quantos
#alunos de fato comerão no bandejão (em dias de comida ruim, pode ser que sobrem
#senhas!). Para tanto, pergunte para quantas pessoas ele está guardando lugar na
#fila e se ele irá continuar na fila (para esta pergunta ele deverá responder ‘S’ ou ‘N’).
#Com essa informação, atualize a fila, inserindo a matrícula daqueles que ainda irão
#chegar e removendo aqueles que vão sair da fila. Imprima a fila final, de acordo com
#ordem de chegada (se a fila for maior que 300, remova os excedentes antes de
#imprimir a fila).


#NAAAAAAAAAAO É MINHA, DIREITOS DO GABRIELL

lista_alunos = []
nova_lista = []
for y in range(300):
  matrícula = int(input('Insira sua matrícula: '))
  lista_alunos.append(matrícula)
  #Lugar extra
  q1 = input('''
  S - Sim
  N - Não
  Você vai guarda lugar na fila para mais alguém?
  ''').upper()
  if q1 == 'S':
    #Número de pessoas
    np = int(input('Para quantas pessoas você vai guardar lugar? '))
    if np > 3:
      print('Inválido! O máximo que se pode guardar são 3 lugares.')
      np = int(input('Para quantas pessoas você vai guardar lugar? '))
    for x in range(np):
      lista_alunos.append(0)

#Removendo os extras
if len(lista_alunos) > 300:
  for x in range(len(lista_alunos)):
    num = lista_alunos[x]
    if num != 0:
      nova_lista.append(lista_alunos[x])
else:
  print(lista_alunos)
  
print(nova_lista)
#6. Faça um programa que funciona como uma agenda telefônica. A agenda deve
#ser guardada em uma lista com o seguinte formato: [[‘Ana’, ‘99999-1234’], [‘Bia’,
#‘99999-5678’]]. (Não utilize esses dados. Isso é só um exemplo da estrutura. Leia
#todos os dados do teclado). O programa deve ter um menu que tenha as seguintes
#opções:
#(a) Adicionar telefones na agenda -- isso deve ser feito de forma que ela se
#mantenha sempre ordenada
#(b) Procurar um telefone -- o usuário informa um nome e o programa mostra o
#número do telefone, ou diz que não está na agenda
#A busca deve ser inteligente: deve parar assim que encontrar um nome maior do
#que o nome que está sendo buscado, ao invés de percorrer a lista sempre até o final
#para concluir que um nome não está na agenda.

agenda = [[0 for j in range(2)] for i in range(10)]
cont = 0
while True:
    print("--------------------O QUE DESEJA FAZER?---------------------")
    print("--------------- 1) Para adicionar um contato----------------")
    print("--------------- 2) Para buscar um Telefone------------------")
    print("------------------- 3) Parar a execução---------------------")

    N = int(input())
    if N == 3:
        print("SAINDO...")
        break
    elif N == 1:
        nome, telefone = input("DIGITE: NOME TELEFONE: ").split()
        agenda[cont][0] = nome 
        agenda[cont][1] = telefone
        print("INSERIDO COM SUCESSO")
    elif N ==2:
        s = input("DIGITE O NOME A SER PESQUISADO: ")
        for i in range(len(agenda)):
            if s == agenda[i][0]:
                print("TELEFONE")
                print(agenda[i][1])
    else:
        print("OPÇÃO INVÁLIDA")

    cont += 1
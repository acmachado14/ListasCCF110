#13. Fazer um algoritmo que:
#a)Leia um vetor A com 30 valores numéricos distintos;
#b)Leia outro vetor B com 30 valores numéricos;
#c)Leia o valor de uma variável X;
#d)Verifique qual o elemento de A que é igual a X;
#e)Escreva o elemento de B de posição correspondente à do elemento de A igual a X.


A = [] 
B = []

#a) -----------------------------------------------------------------------------------------
for i in range(5):
    A.append(int(input(f"Informe o numero da posição A[{i+1}]: ")))
while True:  #Variaveis distintas = variaveis diferentes
    cont = 0
    for k in range(len(A)):
        if A[i] == A[k]:
            cont += 1
    if cont > 1:
        A[i] = int(input("Numero ja cadastrado!! Por favor infome outro numero! "))
    else:
        break

#b) -----------------------------------------------------------------------------------------   
for i in range(5):
     B.append(int(input(f"Informe o numero da posição B[{i+1}]: ")))

#c) -----------------------------------------------------------------------------------------   
x = int(input("Informe o valor da variavel X: "))


#d) -----------------------------------------------------------------------------------------  
i = 0
posicao = -10 #numero aleatorio para fazer a ferificação no IF la em baixo
while True:
    if A[i] == x:
        print(f"O elemento que é igual a X é: A[{i+1}] = {A[i]}")
        posicao = i
        break
    i += 1


#e) -----------------------------------------------------------------------------------------  
#Aqui verifico se foi encontrado o numero X no vetor A[]
if posicao == -10:
    print("Nao exite o numero X em A[]")
else:
    print(f"A posição de B correspondente correspondente à do elemento de A igual a X é: {B[posicao]}")
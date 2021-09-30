#7. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP
#e gere dois outros arquivos, um contendo os endereços IP válidos e outro contendo
#os endereços inválidos. O formato de um endereço IP é num1.num.num.num, onde
#num1 vai de 1 a 255 e num vai de 0 a 255.

ip = open("ip", 'r')
ip_invalido = open("ip_Invalido", 'w')
ip_valido = open("ip_Valido", 'w')

posicao = 0
cont = 0


for x in ip:
    k = x.split(".")
    vali = 0
    s = ""
    for i in range(len(k)):
        aux = int(k[i])
        aux0 = int(k[0])
        if aux0 >= 1 and aux0<=255 and i == 0:
            vali += 1
        if i != 0 and aux >=0 and aux <= 255:
            vali += 1

        if i == len(k)-1:
            s += str(aux)
        else:
            s += str(aux) + "."

    if vali == 4:
        ip_valido.write(str(s))
        ip_valido.write("\n")
    else:
        ip_invalido.write(str(s))
        ip_invalido.write("\n")

ip.close()
ip_invalido.close()
ip_valido.close()  
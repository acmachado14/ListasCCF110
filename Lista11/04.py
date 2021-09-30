#4. Escreva um programa que receba dois nomes de arquivos e copie o conteúdo do
#primeiro arquivo para o segundo arquivo. Considere que o conteúdo do arquivo de
#origem é um texto. Seu programa não deve copiar linhas comentadas (que
#começam com //)

velho = open("teste", 'r')
novo = open("novo", 'w')

for texto in velho:
    if not ("//" in texto):
        novo.write(texto)

velho.close()
novo.close()

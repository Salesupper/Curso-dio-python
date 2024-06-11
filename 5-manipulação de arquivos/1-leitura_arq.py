arq = open("5-manipulação de arquivos\lore.txt",'r')

# retorna tudo em uma string
# print(arq.read())

# retorna uma linha por vez
# print(arq.readline())

# modo correto readline()
# while len(linha := arq.readline()):
#     print(linha)
# arq.close()

# retorna todas as linhas em lista (necessário iterar)
for linha in arq.readlines():
    print(linha)
arq.close()

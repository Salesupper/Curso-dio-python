arq = open('5-manipulação de arquivos/teste.txt', 'w')

# escrever apenas uma palavra
arq.write('escrevendo dados em um arquivo')

# escrever frase ou texto (iterável, para listas)
arq.writelines(['\nescrevendo ','um ','novo ','texto'])
arq.close()
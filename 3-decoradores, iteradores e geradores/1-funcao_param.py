def msg(nome):
    print('executando msg...')
    return f'oi {nome}'

def msg_longa(nome):
    print('executando msg longa...')
    return f'olá tudo bem com vc, {nome}'

# argumeto chumbado  
# def executar(funcao):
#     print('executando executar...')
#     return funcao('rafa')

def executar(funcao,nome):
    print('executando executar...')
    return funcao(nome)

print(executar(msg,'John'))
print(executar(msg_longa,'John'))
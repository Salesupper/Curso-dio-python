def meu_decorador(funcao):
    def envelope():
        print('faz algo antes de executar')
        funcao()
        print('faz algo depois de executar')

    return envelope

'''
# sem açucar sintatico
def ola_mundo():
    print('Olá mundo!')

modo sem decorador
ola_mundo()

# modo com decorador
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
'''

#com açucar sintatico
@meu_decorador
def ola_mundo():
    print('Olá mundo!')

ola_mundo()
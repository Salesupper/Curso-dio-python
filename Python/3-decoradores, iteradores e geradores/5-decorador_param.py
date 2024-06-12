'''
*args (argumentos posicionais): Permite que uma função aceite um número arbitrário 
de argumentos posicionais.Quando uma função é chamada com *args, 
os argumentos posicionais passados para a função são coletados em uma tupla. 
Isso é útil quando você não sabe quantos argumentos serão passados para a função.
**kwargs (argumentos de palavra-chave): Permite que uma função aceite um número arbitrário de 
argumentos de palavra-chave (ou chave-valor). Quando uma função é chamada com **kwargs, 
os argumentos de palavra-chave passados para a função são coletados em um dicionário. 
Isso é útil quando você precisa aceitar argumentos de palavra-chave arbitrários.
'''

# decorador com parametros
def meu_decorador(funcao):
    def envelope(*args,**kwargs):
        print('faz algo antes de executar')
        funcao(*args,**kwargs)
        print('faz algo depois de executar')

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f'olá mundo! {nome}')

ola_mundo('John')
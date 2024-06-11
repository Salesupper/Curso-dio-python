import functools

# decorador com introspecção
def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args,**kwargs):
        print('faz algo antes de executar')
        retorno = funcao(*args,**kwargs)
        print('faz algo depois de executar')
        return retorno
    
    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f'olá mundo! {nome}')
    return nome.upper()

print(ola_mundo.__name__)
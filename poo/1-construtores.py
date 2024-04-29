class Bicicleta:
    # construtor
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('bi bi!!!')

    def correr(self):
        print('a bicicleta está correndo')

    def parar(self):
        print('a bicicleta parou')
    
    def get_cor(self):
        return self.cor

    def __str__(self):
        return f'{self.__class__.__name__}: {[f"{chave}={valor}" for chave, valor in self.__dict__.items()]}'

    # destrutor (destroi a classe) ninguem usa
    # def __del__(self):
    #     print('destruindo a instancia')

b1 = Bicicleta('verde','bmx',2012,2000.00)

# b2 = Bicicleta('roxo','cross',2015,1547.90)
# del b2

print(b1.buzinar())
print(b1.get_cor())
print(b1.cor,b1.ano,b1.modelo,b1.valor)
print(b1)



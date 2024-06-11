class Iterador:
    def __init__(self,lista: list[int]):
        self.lista = lista
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.lista[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in Iterador([2,2,4]):
    print(i)
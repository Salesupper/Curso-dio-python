class Passaro:
    def voar(self):
        print('voando')

class Pardal(Passaro):
    # def voar(self):
    #     super().voar()
    def voar(self):
        print('pardal voando')

class Avestruz(Passaro):
    def voar(self):
        print('avestruz não voa')

# FIXME exemplo ruim do uso de herança para obter o metodo voar
class Aviao(Passaro):
    def voar(self):
        print('Aviâo decolando')

def voos(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

voos(p1)
voos(p2)
voos(p3)
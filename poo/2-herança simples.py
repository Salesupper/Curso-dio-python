class Veiculo:
    def __init__(self,cor,placa,num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print('ligando motor')

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,cor,placa,num_rodas,carregado):
        super().__init__(cor,placa,num_rodas)
        self.carregado = carregado
    
    def com_carga(self):
        if self.carregado == False:
            print('está vazio')
        else:
            print('está cheio')

m1 = Moto('azul','m2x-500',2)
car = Carro('prata','zx3-234',4)
cam = Caminhao('vermeho','g3c-758',6,True)

m1.ligar_motor()
print(m1.cor)
car.ligar_motor()
print(car.placa)
cam.ligar_motor()
print(cam.num_rodas)
cam.com_carga()


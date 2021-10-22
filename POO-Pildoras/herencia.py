class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Maca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, 
        "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):  #Se está aplicando la herencia desde la clase Vehiculos a Furgoneta

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
        

class Moto(Vehiculos): #Se está aplicando la herencia desde la clase Vehiculos a Moto
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    #Se sobre escribe el Método estado con la herencia y el método propio de la clase
    def estado(self):
        print("Maca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, 
        "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        
        super().__init__(marca, modelo)
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True



miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kagoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

miBici=BicicletaElectrica("Orbea", "cxc")

class Coche():

    def desplazamiento(self):
        print("Me desplazo usando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo usando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo usando seis ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)
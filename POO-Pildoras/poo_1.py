class Coche():
    def __init__(self): #Método constructor

        self.__largoChasis=250  #Variable encapsulada
        self.__anchoChasis=120  #Variable encapsulada
        self.__ruedas=4 #Variable encapsulada
        self.__enmarcha=False  #Variable encapsulada

    #Estos son los métodos de las acciones que realizan los objetos
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__cheque_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"

        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal, no podemos arrancar"

        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene:", self.__ruedas, "ruedas. Un ancho de:", self.__anchoChasis, "y un largo de ",
        self.__largoChasis)

    def __cheque_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        
        else:
            return False


miCoche=Coche() #Este es un objeto con la instancia a su clase
print(miCoche.arrancar(True))
miCoche.estado()

print("----------------------A continuación creamos el segundo objeto----------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

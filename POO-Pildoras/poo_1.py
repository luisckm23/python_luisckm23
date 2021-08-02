class Coche():
    def __init__(self): #Metodo constructor __init__ da ESTADO inicial al objeto.
        self.__largoChasis = 250   #Propiedades/ Poniento guiones bajos antes de la variable se ENCAPSULA y es accesible desde la propia clase
        self.__anchoChasis = 120   #Propiedades/ Poniento guiones bajos antes de la variable se ENCAPSULA  y es accesible desde la propia clase
        self.__ruedas = 4          #Propiedades / Poniento guiones bajos antes de la variable se ENCAPSULA  y es accesible desde la propia clase
        self.__enmarcha = False    #Propiedades/ Poniento guiones bajos antes de la variable se ENCAPSULA  y es accesible desde la propia clase

    
    def arrancar(self, arrancamos): #Método de la clase Coche
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno() #Se está utilizando un Método encapsulado

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal"

        else:
            return "El coche está parado"
    
    def estado(self): #Método que solamente imprime el estado del coche
        print("El coche tiene ", self.__ruedas, " ruedas", " un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    #Encapsulamiento de un MÉTODO es con dos giones bajo (__) delante del nombre del metodo para usarlo desde la clase que lo utiliza y no desde otra clase
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

print("Se crea el primer OBJETO de la clase Coche-------------------")

miCoche=Coche() #Instaciacion de clase 
print(miCoche.arrancar(True))

miCoche.estado()


print("Se crea el segundo OBJETO de la clase Coche-----------------")
miCoche2=Coche() #Instanciacion de clase
print(miCoche2.arrancar(False))
miCoche2.estado()

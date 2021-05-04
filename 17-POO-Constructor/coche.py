#Programación Orientada a Objetos
# Constructor. Es un Método especial dentro de una clase que se utiliza 
# para dar un valor a los Atributos del objeto al crearlo
#Definir una clase, molde para crear más objetos de ese tipo (coche)
#Coche con características similares


class Coche:

    #Atributos/Propiedades (variables)
    #Caracteristicas del Coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Visibilidad de los métodos
    soy_publico = "Hola soy un atributo publico" #Se puede tomar el método desde cualquier parte del codigo
    __soy_privado = "Soy un atributo privado" #Se inicia con __ para decir que es privado

    #Constructor con los atributos del objeto
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo 
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #Métodos son acciones que hace el objeto(funciones)
    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color 
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo 
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad +=  1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        
        info = " ---------Informacion del coche----------- "
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo " + self.getModelo()
        info += "\n Velocidad " + str(self.getVelocidad())

        return info
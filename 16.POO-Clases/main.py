#Programación Orientada a Objetos

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

    #Métodos son acciones que hace el objeto(funciones)
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color 
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo 

    def acelerar(self):
        self.velocidad +=  1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
#Fin de definicion de clase

#Crear objetos / Instanciar la clase
coche = Coche()
print("COCHE 1") 
coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar() #Metodo
coche.acelerar() #Metodo
coche.acelerar() #Metodo
coche.acelerar() #Metodo
coche.frenar() #Metodo

print("Velocidad actual: ", coche.velocidad)

#Crear mas objetos
print("-----------------------------------")
print("Coche 2")
coche2 = Coche() 
coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))
"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre
que pueden usarse invocando a la función tantas veces como sea necesario

def nombreDeMiFuncion (parámetro):
    conjunto de instrucciones

nombreDeMiFuncion (parámetro)
"""

### Ejemplo 1

print("# # # Ejmplo 1 # # #")

def muestraNombre():
    print("Luis")
    print("Rodrigo")
    print("Juan")
    print("José")
    print("\n")

#Invocar funciones
muestraNombre()


### Ejemplo 2

print("\n# # # Ejmplo 2 # # #")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")

    if edad >= 18:
        print("Eres mayor de edad ")
    else:
        print(f"Eres menor de edad ")

nombre = input("\nEscribe tu nombre: ")
edad = int(input("Ingresa la edad que tienes : "))
mostrarTuNombre(nombre, edad)

### Ejemplo 3

print("\n# # # Ejmplo 3 # # #")

def tabla(numero):
    print(f"La tabla de multiplicar del numero {numero}")
    
    for contador in range (1 , 11):
        operacion = numero * contador
        print(f"{numero} x {contador} =  {operacion}")
    
    print("\n")
numero = int(input("Ingresa un numero para hacer la tabla que quieres: "))
tabla(numero)

## Ejemplo 3.1

print("\n# # # Ejmplo 3.1 # # #")

for numero_tabla in range (1, 11):
    tabla(numero_tabla)

## Ejemplo 4

print("\n# # # Ejmplo 4 # # #")
print("# # # Parámetros opcionales # # #")

def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Empleado: {nombre}")
    
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Luis")

## Ejemplo 5

print("\n# # # Ejmplo 5 # # #")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Luis"))


## Ejemplo 6

print("\n# # # Ejmplo 6 # # #")
print("\n# # # CALCULADORA # # #")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n" 
    else:    
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(div)

    return(cadena)

print(calculadora(5, 5))

## Ejemplo 7

print("\n# # # Ejmplo 7 # # #")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    apellidos =f"El apellido es: {apellidos}"
    return apellidos

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Luis", "Juárez"))


## Ejemplo 8

print("\n# # # Ejmplo 8 # # #")
print("\n# # # FUNCION L A M D A # # #")

dime_el_anio = lambda year: f"El año es: {year}"

print(dime_el_anio(2034))



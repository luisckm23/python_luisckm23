"""
Una función es un conjunto de instrucciones agrupadas bajo un nombre
que pueden usarse invocando a la función tantas veces como sea necesario

def nombreDeMiFuncion (parámetro):
    conjunto de instrucciones

nombreDeMiFuncion (mi_parámetro)
"""
"""""
#Ejemplo 1 Definiendo funcion
print("Ejemplo 1")

def muestraNombre():
    print("Luis")
    print("Paco")
    print("Juan")
    print("Nestor")
    print("\n")

#Invocar funcion
muestraNombre()

#Ejemplo 2 Parámetros
print("Ejemplo 2")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Eres menos de edad")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Escribe tu edad: "))

mostrarTuNombre(nombre, edad)

#Ejemplo 3 
print("\nEjemplo 3")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range (1, 11, 2):
        operacion = numero * contador
        print(f"{numero} * {contador} = {operacion}")

numero = int(input("Ingresa el numero para hacer la tabla: "))
tabla(numero)
"""""
#Ejemplo 4
print("\nEjemplo 4")

def sum():
    num1=int(input("Escribe el primer numero para sumar: "))
    num2=int(input("Escribe el segundo numero para sumar: "))
    resultado = num1+num2
    print(f"La suma de {num1} + {num2} es: {resultado}")

sum()

def suma(num1, num2):
    resultado = num1 + num2

    return resultado
print(suma(5,7))
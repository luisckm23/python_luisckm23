"""
Hacer un programa de una lista de 8 numeros enteros:

Recorrer la lista y mostrarla
Hacer función para recorrer la lista y devuelva un string
Ordenarla y mostrarla
Mostar la longitud
Buscar un elemento que el usuario pida por teclado

"""

#Crear Lista

numeros = [13, 64, 52, 73, 21, 7, 91, 63]

def mostrarLista(lista):
    resultado =""
    for elemento in lista:
        resultado += "Elementos: " + str(elemento)
        resultado  += "\n"
    return resultado


#Recorrer y mostrar la lista
print("Recorrer y mostrar la lista")
"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))

#Ordenar y mostrar la lista
print("Ordenar y mostar la lista")

numeros.sort()
print(mostrarLista(numeros))

#Mostrar la longitud de la lista
print("Mostrar la longitud de la lista")

print(len(numeros))

#Buscar un elemento por teclado
print("Buscar numero por teclado")

busqueda = int(input("Introduce el numero a buscar: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero a buscar: "))
else: 
    print(f"Has ingresado el {busqueda}")

print(f"### Buscar en la lista el número {busqueda} ####")

search = numeros.index(busqueda)

print(f"El numero buscado existe en la lista, es el indice: {search}")

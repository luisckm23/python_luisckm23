#Son inmutables, no se pueden modificar después de su creación
#No permite añadir, eliminar, mover elementos
#No permiten búsquedas
#Sí permiten extraer porciones, pero el resultado es una nueva tupla
#Sí permiten comprobar si un elemento está en una tupla

#Sintaxis nombreTupla=(elem1, elem2, elem3...)
print("\nEsto es una tupla")
mitupla = ("Juan", 13,1, 1995)
print(mitupla)
print(mitupla[2])

#Metodo para convertir una tupla en lista 
print("\nMetodo para convertir una tupla en lista")
milista = list(mitupla)
print(mitupla)
print(milista)

#Metodo para convetir una lista en tupla
print("\nMetodo para convertir una lista en tupla")
myList = ["Juan", 13, 1, 1995]
myTuple = tuple(myList)
print(myList)
print(myTuple)

#Metodo para contar elementos en una tupla
print("\nMetodo 'Count' para contar elementos en una tupla")
print(myTuple.count(13))

#Metodo para saber la longitud de una tupla
print("\nMetodo 'len' para saber la longitud de una tupla")
print(len(myTuple))
#La principal característica de los diccionarios es que los datos se almacenan a una clave de tal forma
#que se crea una asociación de tipo CLAVE:VALOR para cada elemento almacenado

#Los elementos almacenados no están ordenados.

#Sintaxis
print("Esta es la sintaxis de un diccionario")
midiccionario = {"Alemania": "Berlín", "Francia":"París", "Reino Unido": "Londres", "España":"Madrid"}
print(midiccionario)

#Mostar un elemento único
print("\nMostar un elemento único")
print(midiccionario["Francia"])

#Agregar elementos a un diccionario construido
print("\nAgregar elementos a un diccionario construido")
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#Modificar elementos a un diccionario construido
print("\nModificar elementos a un diccionario construido")
midiccionario["Italia"]="Roma"
print(midiccionario)

#Eliminar elementos a un diccionario construido
print("\nEliminar elementos a un diccionario construido")
del midiccionario["Reino Unido"]
print(midiccionario)

#Diccionario con diferentes tipos 
print("\nDiccionario con diferentes tipos ")
mydictionary = {"Alemania": "Berlín", 23:"Jordan", "Mosqueteros":3}
print(mydictionary)

#Asignar valores a una tupla
print("\nAginar valores a una tupla")
mitupla = ("España", "Francia", "Reino Unido", "Alemania")
diccionario ={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Liverpool", mitupla[3]:"Frankfurt"}
print(diccionario)

#Almacenar una tupla en un diccionario
print("\nAlmacenar un diccionario en una tupla")
midic ={23:"Jordan", "Nombre":"Michale", "Equipo": "Chicago", "anillos":{"temporadas":(1991, 1992, 1993, 1996,1997,1998)}}
print(midic)
print(midic["anillos"])

#Metodo para devolver las claves de un diccionario
print("\nMetodo para devolver las claves de un diccionario")
print(midic.keys())

#Metodo para devolver los valores de un diccionario
print("\nMetodo para devolver los valores de un diccionario")
print(midic.values())

#Metodo para devolver la longitud
print("\nMetodo para devolver la longitud")
print(len(midic))